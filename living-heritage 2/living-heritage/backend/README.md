# Backend (M2 — Node/Express)

## Current state: foundation only

A minimal Express server with one route, `GET /api/health`. No database
connection, no authentication, no other routes yet — see `docs/API.md`
at the project root for the full (currently tiny) API reference.

## Setup

```bash
cd backend
npm install
npm start
```

Then check it's up:

```bash
curl http://localhost:4000/api/health
# {"status":"ok"}
```

## Planned (not built yet)

Routes for citizens/traditions/town state, a PostgreSQL connection, and
whatever the simulation engine needs to expose once it's further along.
