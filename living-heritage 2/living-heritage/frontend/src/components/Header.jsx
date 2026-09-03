// Simple top bar. No props yet - just a static title until there's real
// town data (name, in-game date, etc.) to show here.
function Header() {
  return (
    <header className="flex h-16 shrink-0 items-center border-b border-gray-200 bg-white px-6">
      <h1 className="text-lg font-semibold text-gray-800">Living Heritage</h1>
      <span className="ml-2 text-sm text-gray-400">Town Simulator (MVP)</span>
    </header>
  )
}

export default Header
