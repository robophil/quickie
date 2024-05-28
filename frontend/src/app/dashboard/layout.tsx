import DashboardAside from '../components/DashboardAside'
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className='flex flex-row h-full w-full'>
      <aside className='h-full'>
        <DashboardAside />
      </aside>
      <main className='h-full'>{children}</main>
    </div>
  )
}