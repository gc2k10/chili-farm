"""Print averaged ADC readings from a soil sensor connected to GP26."""

from machine import ADC, Pin
from time import sleep_ms

SENSOR_PIN = 26
SAMPLE_COUNT = 5
SAMPLE_INTERVAL_MS = 50
READING_PAUSE_MS = 1000


def main():
    sensor = ADC(Pin(SENSOR_PIN))
    print("adc_u16")
    while True:
        total = 0
        for _ in range(SAMPLE_COUNT):
            total += sensor.read_u16()
            sleep_ms(SAMPLE_INTERVAL_MS)
        print(total // SAMPLE_COUNT)
        sleep_ms(READING_PAUSE_MS)


if __name__ == "__main__":
    main()
