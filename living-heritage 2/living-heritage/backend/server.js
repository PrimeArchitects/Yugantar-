// Minimal Express server for Living Heritage.
//
// Right now this only exposes a health check so the frontend (and the
// team) can confirm the backend is running. Real endpoints (citizens,
// traditions, town state, ...) get added once the simulation and
// database exist for them to read from.

import express from 'express'

const app = express()
const PORT = process.env.PORT || 4000

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok' })
})

app.listen(PORT, () => {
  console.log(`Living Heritage backend running at http://localhost:${PORT}`)
})
