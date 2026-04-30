'use client'

import { useActionState } from 'react'
import Link from 'next/link'
import { useSearchParams } from 'next/navigation'
import { login } from '@/app/actions/auth'

export default function LoginPage() {
  const [state, action, pending] = useActionState(login, undefined)
  const searchParams = useSearchParams()
  const activated = searchParams.get('activated')
  const errorParam = searchParams.get('error')

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md bg-white rounded-2xl shadow p-8 space-y-6">
        <h1 className="text-2xl font-bold text-center">登录</h1>

        {/* 激活成功提示 */}
        {activated && (
          <p className="text-sm text-green-600 bg-green-50 border border-green-200 rounded p-3 text-center">
            账号激活成功！请登录
          </p>
        )}

        {/* token 无效提示 */}
        {errorParam === 'invalid_token' && (
          <p className="text-sm text-red-500 bg-red-50 border border-red-200 rounded p-3 text-center">
            激活链接已失效或已使用，请重新注册
          </p>
        )}

        {/* 全局错误 */}
        {state?.message && (
          <p className="text-sm text-red-500 bg-red-50 border border-red-200 rounded p-3 text-center">
            {state.message}
          </p>
        )}

        <form action={action} className="space-y-4">
          {/* 邮箱 */}
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
              邮箱
            </label>
            <input
              id="email"
              name="email"
              type="email"
              placeholder="example@email.com"
              className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {state?.errors?.email && (
              <p className="mt-1 text-xs text-red-500">{state.errors.email[0]}</p>
            )}
          </div>

          {/* 密码 */}
          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-1">
              密码
            </label>
            <input
              id="password"
              name="password"
              type="password"
              placeholder="请输入密码"
              className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {state?.errors?.password && (
              <p className="mt-1 text-xs text-red-500">{state.errors.password[0]}</p>
            )}
          </div>

          <button
            type="submit"
            disabled={pending}
            className="w-full bg-blue-600 text-white rounded-lg py-2 font-medium hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition"
          >
            {pending ? '登录中…' : '登录'}
          </button>
        </form>

        <p className="text-sm text-center text-gray-500">
          还没有账号？{' '}
          <Link href="/register" className="text-blue-600 hover:underline">
            去注册
          </Link>
        </p>
      </div>
    </div>
  )
}
