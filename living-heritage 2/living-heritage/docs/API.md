# API

Base URL (local development): `http://localhost:4000`

Only one endpoint exists so far. This file will grow as backend routes
are added (citizens, traditions, town state, events, policies, ...).

---

## `GET /api/health`

Confirms the backend server is running.

**Request**

No parameters, no body.

**Response** — `200 OK`

```json
{ "status": "ok" }
```

**Example**

```bash
curl http://localhost:4000/api/health
```
