# Living Heritage — SIH MVP

An AI-assisted, agent-based simulation of an Indian heritage-inspired virtual
town. Citizens live, work, raise families, and pass cultural traditions to
the next generation. Players (through policies and events) try to keep
traditions alive while the town's economy grows.

This is an MVP — the goal is a small, working, explainable simulation, not a
polished product.

## Repo layout

```
living-heritage/
├── simulation/     # M3 — Python simulation engine (the "brain": citizens,
│                   #      clock, culture, economy, events, policies)
├── backend/        # M2 — Node/Express API (serves simulation state to the UI)
├── frontend/       # M1 — React + Vite + Tailwind (UI, Recharts, Leaflet map)
├── database/       # M4 — PostgreSQL schema, migrations, seed data
├── ai-advisor/     # M5 — AI advisor, controlled event generation, explanations
└── docs/           # M6 — culture reference notes, sources, QA checklists
```

Only `simulation/` has real code so far. The other folders are placeholders
until we reach them in the build order below — we're avoiding building
scaffolding before it's needed.

## Tech stack

| Layer            | Tech                          | Owner |
|-------------------|-------------------------------|-------|
| Frontend          | React, Vite, Tailwind, Recharts, Leaflet | M1 |
| Backend API       | Node.js, Express              | M2 |
| Simulation engine | Python (standard library only, for now) | M3 |
| Database          | PostgreSQL                    | M4 |
| AI                | Used only where it adds value: advisor chat, controlled/generated events, plain-language explanations. Never used to invent cultural facts. | M5 |
| Culture / QA / Integration | Cross-cutting, keeps facts accurate, tests the whole system | M6 |

**How the pieces will connect (planned, not all built yet):** the Python
simulation engine advances the town's state (a tick = one time step). The
Node/Express backend will call the simulation engine and store/read state in
PostgreSQL, then serve it to the React frontend as a normal REST API. We'll
nail down the exact call mechanism (subprocess vs. small internal API) when
we get to the "backend" step, once we know what the simulation actually
needs to expose.

## Build order

We build one feature at a time, in this order:

1. **Citizen** ← we are here
2. Simulation clock
3. Culture (traditions)
4. Cultural transmission
5. Economy
6. Events / festivals
7. Policies
8. UI
9. Backend
10. Database
11. Integration
12. AI advisor
13. Analytics
14. Testing (ongoing throughout, but hardened at the end)

## Ground rules

- Beginner-friendly code over clever code.
- Minimal dependencies — add a package only when we actually need it.
- No secrets in code (API keys, DB passwords, etc. go in `.env` files, which
  are git-ignored).
- Don't invent cultural facts — anything about a real tradition must come
  from a cited source (M6 owns this).
- One feature at a time, with a short plan before building and a test +
  report after.
