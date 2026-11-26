# ChiliFarm

<img src="frontend/assets/brand/chilifarm-original.png" alt="ChiliFarm logo" width="480">

[Project website](https://gc2k10.github.io/chili-farm/about.html) · [Interactive demo](https://gc2k10.github.io/chili-farm/)

A modular, self-hosted smart growing project for chili peppers, starting with a single Naga Jolokia plant.

ChiliFarm combines Raspberry Pi Pico 2 W, MicroPython, soil sensing, grow lighting and planned automated irrigation. A Raspberry Pi 5 will eventually host measurement history and a responsive dashboard.

## Project status

Early prototype — not production-ready.

| Component | Status |
|---|---|
| Grow lighting | Hardware selected; schedule verification pending |
| Soil sensing | Diagnostic script available; hardware validation pending |
| Irrigation | Planned; assembly and safety testing pending |
| Local display and environmental sensing | Planned |
| Telemetry and dashboard | Planned |
| Plant photography | Planned |

## Getting started

1. Review the [hardware and architecture](docs/hardware.md).
2. Follow the [commissioning and calibration guide](docs/commissioning.md) with the pump disconnected.
3. Run [the MicroPython diagnostic](firmware/read_soil.py) manually in Thonny.
4. Record measurements and validate the sensor before attempting irrigation.

## Safety

Keep water away from electronics. Verify voltage levels, pump driver compatibility and flyback protection. Never enable unattended watering before testing fail-safe behavior and runtime limits.

## Roadmap

See the [development roadmap](docs/roadmap.md). Contributions and feedback are welcome through GitHub Issues. Please do not include credentials or private infrastructure details.

## License and support

Licensed under the [MIT License](LICENSE). Optional support: [Buy Me a Coffee](https://buymeacoffee.com/gc2k10f). No payment is required to view this repository.

