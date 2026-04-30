'use server'

import { redirect } from 'next/navigation'
import bcrypt from 'bcrypt'
import { randomBytes } from 'crypto'
import { Resend } from 'resend'
import pool from '@/app/lib/db'
import { createSession, deleteSession } from '@/app/lib/session'
import {
  RegisterSchema,
  LoginSchema,
  RegisterFormState,
  LoginFormState,
} from '@/app/lib/definitions'

const resend = new Resend(process.env.RESEND_API_KEY)

// ========== 注册 ==========
export async function register(
  state: RegisterFormState,
  formData: FormData
): Promise<RegisterFormState> {
  // 1. 校验表单
  const result = RegisterSchema.safeParse({
    user: formData.get('user'),
    email: formData.get('email'),
    password: formData.get('password'),
  })

  if (!result.success) {
    return { errors: result.error.flatten().fieldErrors }
  }

  const { user, email, password } = result.data

  // 2. 检查用户名或邮箱是否已被注册
  const [rows] = await pool.execute(
    'SELECT id FROM users WHERE user = ? OR email = ?',
    [user, email]
  )
  if ((rows as unknown[]).length > 0) {
    return { message: '用户名或邮箱已被注册' }
  }

  // 3. 密码哈希后写入数据库
  const hashedPassword = await bcrypt.hash(password, 10)
  const [insertResult] = await pool.execute(
    'INSERT INTO users (user, email, password, is_active) VALUES (?, ?, ?, FALSE)',
    [user, email, hashedPassword]
  )
  const userId = (insertResult as { insertId: number }).insertId

  // 4. 生成激活 token（64 位随机十六进制字符串）
  const token = randomBytes(32).toString('hex')
  const expiresAt = new Date(Date.now() + 24 * 60 * 60 * 1000) // 24 小时有效
  await pool.execute(
    'INSERT INTO activation_tokens (token, user_id, expires_at) VALUES (?, ?, ?)',
    [token, userId, expiresAt]
  )

  // 5. 发送激活邮件
  const activationUrl = `${process.env.NEXT_PUBLIC_APP_URL}/api/auth/activate?token=${token}`
  await resend.emails.send({
    from: process.env.EMAIL_FROM!,
    to: email,
    subject: '激活你的账号',
    html: `
      <h2>欢迎注册！</h2>
      <p>点击下方链接激活你的账号（链接 24 小时内有效）：</p>
      <a href="${activationUrl}">${activationUrl}</a>
    `,
  })

  // 6. 跳转到"请查收邮件"页面
  redirect('/verify-email')
}

// ========== 登录 ==========
export async function login(
  state: LoginFormState,
  formData: FormData
): Promise<LoginFormState> {
  // 1. 校验表单
  const result = LoginSchema.safeParse({
    email: formData.get('email'),
    password: formData.get('password'),
  })

  if (!result.success) {
    return { errors: result.error.flatten().fieldErrors }
  }

  const { email, password } = result.data

  // 2. 查找用户
  const [rows] = await pool.execute(
    'SELECT id, password, is_active FROM users WHERE email = ?',
    [email]
  )
  const user = (rows as { id: number; password: string; is_active: number }[])[0]

  // 故意不区分"用户不存在"和"密码错误"，防止枚举攻击
  if (!user) {
    return { message: '邮箱或密码错误' }
  }

  // 3. 检查是否已激活
  if (!user.is_active) {
    return { message: '账号尚未激活，请检查邮箱' }
  }

  // 4. 验证密码
  const passwordMatch = await bcrypt.compare(password, user.password)
  if (!passwordMatch) {
    return { message: '邮箱或密码错误' }
  }

  // 5. 创建 session（写 cookie）
  await createSession(user.id)

  redirect('/dashboard')
}

// ========== 登出 ==========
export async function logout(): Promise<void> {
  await deleteSession()
  redirect('/login')
}
