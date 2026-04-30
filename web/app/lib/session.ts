import 'server-only'
import { SignJWT, jwtVerify } from 'jose'
import { cookies } from 'next/headers'

const key = new TextEncoder().encode(process.env.JWT_SECRET)

// JWT 有效期：7 天
const SESSION_DURATION = 7 * 24 * 60 * 60 * 1000

export type SessionPayload = {
  userId: number
  expiresAt: Date
}

// 生成 JWT
export async function encrypt(payload: SessionPayload): Promise<string> {
  return new SignJWT({ userId: payload.userId, expiresAt: payload.expiresAt.toISOString() })
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('7d')
    .sign(key)
}

// 验证并解析 JWT
export async function decrypt(token: string | undefined): Promise<SessionPayload | null> {
  if (!token) return null
  try {
    const { payload } = await jwtVerify(token, key, { algorithms: ['HS256'] })
    return {
      userId: payload.userId as number,
      expiresAt: new Date(payload.expiresAt as string),
    }
  } catch {
    return null
  }
}

// 登录成功后调用：写 cookie
export async function createSession(userId: number): Promise<void> {
  const expiresAt = new Date(Date.now() + SESSION_DURATION)
  const token = await encrypt({ userId, expiresAt })
  const cookieStore = await cookies()
  cookieStore.set('session', token, {
    httpOnly: true,                                       // JS 无法读取，防 XSS
    secure: process.env.NODE_ENV === 'production',        // 生产环境强制 HTTPS
    expires: expiresAt,
    sameSite: 'lax',
    path: '/',
  })
}

// 读取当前登录用户
export async function getSession(): Promise<SessionPayload | null> {
  const cookieStore = await cookies()
  const token = cookieStore.get('session')?.value
  return decrypt(token)
}

// 登出时调用
export async function deleteSession(): Promise<void> {
  const cookieStore = await cookies()
  cookieStore.delete('session')
}
