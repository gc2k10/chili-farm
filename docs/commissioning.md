# Prototype commissioning

## 1. USB sensor diagnostics

Install MicroPython for Pico 2 W. Disconnect the GFX Pack and pump circuit for the first test. With USB disconnected, connect the sensor. The prototype uses GP26 / ADC0. Verify wiring against the documentation for your SEN0193 revision and confirm the output voltage is within the ADC input range.

| SEN0193 | Pico 2 W |
|---|---|
| VCC | 3V3(OUT) |
| GND | GND |
| AOUT | GP26 / ADC0 |

Connect Pico over USB and run [read_soil.py](../firmware/read_soil.py) in Thonny. The console prints the average of five samples. Run manually at this stage.

## 2. Pot-specific calibration

1. Place the probe in a representative location and record its position. Do not immerse the sensor electronics.
2. Record readings at the soil moisture level where watering would normally be considered.
3. Water manually, allow water to distribute and excess to drain, then record another series.
4. Repeat across several cycles. Compare direction and variability. ADC values depend on probe, soil and placement.
5. Record ranges and conditions in the [measurement log](../examples/soil-log.csv).

## 3. Pump test outside the pot

Secure tubing and direct the outlet into a graduated container. Measure volume over several short runs. Check for siphoning after shutdown. Before automated testing, verify float switch behavior when full, empty and disconnected. Confirm the pump remains off after controller restart.

Supervise initial automation tests. Set maximum dose runtime and cooldown using measured flow and soil response. Do not enable unattended operation until fail-safe tests pass.
