# Target architecture

Status: planned, except for the existing soil diagnostic script.

- firmware/: local sensing and fail-safe irrigation control.
- backend/: telemetry ingestion and storage on Raspberry Pi.
- frontend/: responsive dashboard.
- hardware/: verified wiring and bill of materials.
- tests/: automated and hardware validation.

The Pico must enforce pump limits independently of network availability. See [hardware](hardware.md) and [roadmap](roadmap.md).
