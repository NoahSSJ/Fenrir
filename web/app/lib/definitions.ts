import * as z from 'zod'

// ---- 注册表单 ----
export const RegisterSchema = z.object({
  user: z
    .string()
    .min(2, { error: '用户名至少 2 个字符' })
    .max(50, { error: '用户名最多 50 个字符' })
    .trim(),
  email: z.email({ error: '请输入有效的邮箱地址' }).trim(),
  password: z
    .string()
    .min(8, { error: '密码至少 8 个字符' })
    .regex(/[a-zA-Z]/, { error: '密码需包含至少一个字母' })
    .regex(/[0-9]/, { error: '密码需包含至少一个数字' })
    .trim(),
})

export type RegisterFormState =
  | {
      errors?: {
        user?: string[]
        email?: string[]
        password?: string[]
      }
      message?: string
    }
  | undefined

// ---- 登录表单 ----
export const LoginSchema = z.object({
  email: z.email({ error: '请输入有效的邮箱地址' }).trim(),
  password: z.string().min(1, { error: '请输入密码' }).trim(),
})

export type LoginFormState =
  | {
      errors?: {
        email?: string[]
        password?: string[]
      }
      message?: string
    }
  | undefined
