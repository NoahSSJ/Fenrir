import Link from 'next/link'

export default function VerifyEmailPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md bg-white rounded-2xl shadow p-8 text-center space-y-4">
        <div className="text-5xl">📬</div>
        <h1 className="text-2xl font-bold">查收激活邮件</h1>
        <p className="text-gray-500 text-sm">
          我们向你的邮箱发送了一封激活邮件，请点击邮件中的链接完成注册。
          <br />
          链接 24 小时内有效。
        </p>
        <p className="text-xs text-gray-400">
          没收到？请检查垃圾邮件箱，或{' '}
          <Link href="/register" className="text-blue-600 hover:underline">
            重新注册
          </Link>
        </p>
      </div>
    </div>
  )
}
