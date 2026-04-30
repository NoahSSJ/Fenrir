'use client'

import { useActionState } from 'react'
import Link from 'next/link'
import { register } from '@/app/actions/auth'

export default function RegisterPage() {
  const [state, action, pending] = useActionState(register, undefined)

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md bg-white rounded-2xl shadow p-8 space-y-6">
        <h1 className="text-2xl font-bold text-center">注册账号</h1>

        {/* 全局错误 */}
        {state?.message && (
          <p className="text-sm text-red-500 bg-red-50 border border-red-200 rounded p-3 text-center">
            {state.message}
          </p>
        )}

        <form action={action} className="space-y-4">
          {/* 用户名 */}
          <div>
            <label htmlFor="user" className="block text-sm font-medium text-gray-700 mb-1">
              用户名
            </label>
            <input
              id="user"
              name="user"
              type="text"
              placeholder="至少 2 个字符"
              className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {state?.errors?.user && (
              <p className="mt-1 text-xs text-red-500">{state.errors.user[0]}</p>
            )}
          </div>

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
              placeholder="至少 8 位，含字母和数字"
              className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {state?.errors?.password && (
              <ul className="mt-1 text-xs text-red-500 space-y-0.5">
                {state.errors.password.map((e) => (
                  <li key={e}>· {e}</li>
                ))}
              </ul>
            )}
          </div>

          <button
            type="submit"
            disabled={pending}
            className="w-full bg-blue-600 text-white rounded-lg py-2 font-medium hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition"
          >
            {pending ? '注册中…' : '注册'}
          </button>
        </form>

        <p className="text-sm text-center text-gray-500">
          已有账号？{' '}
          <Link href="/login" className="text-blue-600 hover:underline">
            去登录
          </Link>
        </p>
      </div>
    </div>
  )
}
