export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div>
      <aside>
        
      </aside>
      <main>{children}</main>
    </div>
  )
}