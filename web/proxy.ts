// Next.js 16 用 proxy.ts 代替了 middleware.ts，负责路由守卫
import { NextRequest, NextResponse } from 'next/server'
import { decrypt } from '@/app/lib/session'
import { cookies } from 'next/headers'

// 需要登录才能访问的路由（前缀匹配）
const protectedPrefixes = ['/dashboard']
// 已登录后不需要再访问的路由（精确匹配）
const authRoutes = ['/login', '/register', '/verify-email']

export default async function proxy(req: NextRequest) {
  const path = req.nextUrl.pathname

  // 读取并解析 session cookie
  const cookieStore = await cookies()
  const token = cookieStore.get('session')?.value
  const session = await decrypt(token)

  const isLoggedIn = !!session?.userId
  const isProtected = protectedPrefixes.some((p) => path.startsWith(p))
  const isAuthRoute = authRoutes.includes(path)

  // 未登录访问受保护页面 → 跳到登录页
  if (isProtected && !isLoggedIn) {
    return NextResponse.redirect(new URL('/login', req.nextUrl))
  }

  // 已登录访问登录/注册页面 → 跳到 dashboard
  if (isAuthRoute && isLoggedIn) {
    return NextResponse.redirect(new URL('/dashboard', req.nextUrl))
  }

  return NextResponse.next()
}

export const config = {
  // 不拦截静态资源和 API 路由
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
}
