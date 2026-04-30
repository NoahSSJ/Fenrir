import { NextRequest, NextResponse } from 'next/server'
import pool from '@/app/lib/db'

// GET /api/auth/activate?token=xxxx
// 用户点击邮件里的链接会到这里
export async function GET(req: NextRequest) {
  const token = req.nextUrl.searchParams.get('token')

  if (!token) {
    return NextResponse.redirect(new URL('/login?error=invalid_token', req.nextUrl))
  }

  // 查找 token（未使用 + 未过期）
  const [rows] = await pool.execute(
    'SELECT user_id FROM activation_tokens WHERE token = ? AND used = FALSE AND expires_at > NOW()',
    [token]
  )
  const record = (rows as { user_id: number }[])[0]

  if (!record) {
    return NextResponse.redirect(new URL('/login?error=invalid_token', req.nextUrl))
  }

  // 激活用户 + 标记 token 已使用（两步放在事务里保证一致性）
  const conn = await pool.getConnection()
  try {
    await conn.beginTransaction()
    await conn.execute('UPDATE users SET is_active = TRUE WHERE id = ?', [record.user_id])
    await conn.execute('UPDATE activation_tokens SET used = TRUE WHERE token = ?', [token])
    await conn.commit()
  } catch (err) {
    await conn.rollback()
    throw err
  } finally {
    conn.release()
  }

  return NextResponse.redirect(new URL('/login?activated=1', req.nextUrl))
}
