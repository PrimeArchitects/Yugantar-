// These are NOT links yet - there's only one real page (Dashboard) so far.
// The rest are shown greyed-out just to indicate where the app is headed;
// they'll become real navigation once those pages exist.
const sections = [
  { label: 'Dashboard', ready: true },
  { label: 'Citizens', ready: false },
  { label: 'Traditions', ready: false },
  { label: 'Economy', ready: false },
  { label: 'Events', ready: false },
]

function Sidebar() {
  return (
    <aside className="w-56 shrink-0 border-r border-gray-200 bg-white p-4">
      <nav className="space-y-1">
        {sections.map((section) => (
          <div
            key={section.label}
            className={
              section.ready
                ? 'rounded-md bg-amber-100 px-3 py-2 text-sm font-medium text-amber-900'
                : 'rounded-md px-3 py-2 text-sm text-gray-400'
            }
          >
            {section.label}
            {!section.ready && (
              <span className="ml-2 text-xs text-gray-300">soon</span>
            )}
          </div>
        ))}
      </nav>
    </aside>
  )
}

export default Sidebar
