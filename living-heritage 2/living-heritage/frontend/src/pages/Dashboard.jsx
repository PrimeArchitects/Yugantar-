// Placeholder page. Once the backend + database are connected, this will
// show real town stats and charts (Recharts) instead of this message.
function Dashboard() {
  return (
    <div className="rounded-lg border border-dashed border-gray-300 bg-white p-10 text-center">
      <h2 className="text-xl font-semibold text-gray-700">Dashboard</h2>
      <p className="mt-2 text-sm text-gray-500">
        This page is a placeholder. Town stats and charts will appear here
        once the simulation, backend, and database are connected.
      </p>
    </div>
  )
}

export default Dashboard
