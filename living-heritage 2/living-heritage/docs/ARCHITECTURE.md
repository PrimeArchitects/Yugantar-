# Architecture

This document describes the project **as it exists right now** — a
foundation only. It will be updated as each build step adds real
functionality.

## Overview

```
┌────────────┐      ┌────────────┐      ┌────────────┐
│  frontend   │ ---> │  backend    │ ---> │  database   │
│  React/Vite │  API │ Node/Express│  SQL │  PostgreSQL │
└────────────┘      └────────────┘      └────────────┘
                            ^
                            | (not connected yet)
                     ┌────────────┐
                     │ simulation  │
                     │  Python     │
                     └────────────┘
```

Nothing above is actually connected to anything else yet — each piece
currently runs completely on its own. Wiring them together is a later
build step (see the top-level `README.md` for the full build order).

## Frontend (`frontend/`)

A minimal React + Vite app styled with Tailwind CSS.

- `src/main.jsx` — mounts the app
- `src/App.jsx` — top-level layout: `Header` + `Sidebar` + page content
- `src/components/Header.jsx` — static top bar
- `src/components/Sidebar.jsx` — static section list (only "Dashboard" is
  a real page right now; the rest are shown greyed-out as "soon")
- `src/pages/Dashboard.jsx` — empty placeholder page

There is no routing library yet (only one page exists), no state
management, and no calls to the backend yet.

## Backend (`backend/`)

A minimal Node.js + Express server with a single route:

- `GET /api/health` → `{ "status": "ok" }`

No database connection, no authentication, and no other routes yet.

## Simulation (`simulation/`)

A Python project, currently in two parts:

- `simulation.py` — an entry-point placeholder that just prints a startup
  message, to confirm the Python environment is set up correctly.
- `src/entities/citizen.py` — the `Citizen` agent (identity, family
  links, job/income, education, cultural knowledge). This exists but is
  **not yet wired into `simulation.py` or anything else** — it's a
  standalone, tested building block for the simulation clock (the next
  real simulation step).

## Database (`database/`)

`schema.sql` currently only contains a placeholder comment. No tables,
no connection from the backend yet.

## Docs (`docs/`)

This folder holds architecture notes (this file), API docs, and (later)
cultural source citations and QA notes.

## What's intentionally NOT built yet

Per the current task scope, none of the following exist yet:

- Simulation logic beyond the standalone `Citizen` entity
- Any AI integration
- Any database tables or connection
- Authentication
- Routing, state management, or API calls in the frontend

These come later, one step at a time.
