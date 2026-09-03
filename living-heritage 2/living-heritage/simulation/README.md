# Simulation engine (M3)

Pure Python. No database, no web framework — this package should always be
runnable and testable completely on its own. That makes it easy to reason
about and easy for other team members (backend, AI) to build on top of
later.

## Layout

```
simulation/
├── requirements.txt
├── simulation.py         # entry-point placeholder (prints a startup message)
├── src/
│   └── entities/
│       └── citizen.py    # the Citizen agent
└── tests/
    └── test_citizen.py
```

`simulation.py` doesn't run any simulation logic yet - it's just a smoke
test confirming Python is set up correctly. Run it with:

```bash
python3 simulation.py
```

More folders (`engine/` for the simulation clock, `culture/`, `economy/`,
`events/`, `policies/`) will be added one at a time, following the build
order in the top-level README.

## Setup

No third-party packages are needed yet (see `requirements.txt` — it's
intentionally near-empty). Just Python 3.9+.

## Running the tests

We're using Python's built-in `unittest` module on purpose — zero installs
required, which matters for a hackathon where six people need to get
running fast.

```bash
cd simulation
python3 -m unittest discover -s tests -v
```
