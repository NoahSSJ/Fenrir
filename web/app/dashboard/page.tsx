import { redirect } from 'next/navigation'
import { getSession } from '@/app/lib/session'
import { logout } from '@/app/actions/auth'
import pool from '@/app/lib/db'

export default async function DashboardPage() {
  // 读取 session，未登录则跳到 /login
  const session = await getSession()
  if (!session) redirect('/login')

  // 获取用户信息（只取需要展示的字段，不返回密码）
  const [rows] = await pool.execute(
    'SELECT user, email FROM users WHERE id = ?',
    [session.userId]
  )
  const user = (rows as { user: string; email: string }[])[0]

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center">
      <div className="bg-white rounded-2xl shadow p-8 w-full max-w-md space-y-4">
        <h1 className="text-2xl font-bold">欢迎回来，{user.user} 👋</h1>
        <p className="text-gray-500 text-sm">邮箱：{user.email}</p>
        <p className="text-gray-400 text-xs">用户 ID：{session.userId}</p>

        {/* 登出按钮：调用 Server Action */}
        <form action={logout}>
          <button
            type="submit"
            className="w-full mt-4 bg-red-500 text-white rounded-lg py-2 font-medium hover:bg-red-600 transition"
          >
            登出
          </button>
        </form>
      </div>
    </div>
  )
}
