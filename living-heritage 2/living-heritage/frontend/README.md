# Frontend (M1 — React / Vite / Tailwind)

## Current state: foundation only

A minimal React + Vite app with Tailwind CSS, a basic layout (`Header` +
`Sidebar` + content area), and one empty `Dashboard` page. Not connected
to the backend yet — that's a later step, once there's real data to show.

## Setup

```bash
cd frontend
npm install
npm run dev
```

Then open the URL Vite prints (usually `http://localhost:5173`).

## Layout

```
frontend/
├── index.html
├── src/
│   ├── main.jsx
│   ├── App.jsx
│   ├── index.css
│   ├── components/
│   │   ├── Header.jsx
│   │   └── Sidebar.jsx
│   └── pages/
│       └── Dashboard.jsx
```

## Planned (not built yet)

Town map (Leaflet), citizen and tradition views, analytics dashboards
(Recharts), event/policy decisions, routing between pages.
