import DashboardAside from '../components/DashboardAside'
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className='flex flex-row h-full w-full'>
      <aside className='h-full p-4'>
        <DashboardAside />
      </aside>
      <main className='h-full p-4'>{children}</main>
    </div>
  )
}