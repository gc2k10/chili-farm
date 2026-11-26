# CHILLI FARM 🌶️

Domowa uprawa Naga Jolokia z doświetlaniem, pomiarem wilgotności podłoża i planowanym podlewaniem z Raspberry Pi Pico 2 W.

Projekt zaczyna się od jednej doniczki. Lampą steruje harmonogram gniazdka Aqara. Pico ma zbierać pomiary, a później uruchamiać pompkę dopiero po sprawdzeniu stanu zbiornika i limitów podlewania. Raspberry Pi 5 ma docelowo przechowywać historię pomiarów i udostępniać panel.

| Element | Etap |
| --- | --- |
| Oświetlenie LED | Dobór lampy i oprawy, konfiguracja niezależnego harmonogramu |
| Wilgotność podłoża | Skrypt odczytu ADC i instrukcja kalibracji |
| Podlewanie | Projekt, montaż i próby do wykonania |
| GFX Pack i Enviro Urban | Planowane wyświetlanie stanu i niezależne pomiary otoczenia |
| Raspberry Pi 5 | Planowana historia pomiarów i panel sterowania |
| Kamera | Planowane zdjęcia wzrostu |

## Od czego zacząć

1. Sprawdź [sprzęt i architekturę](docs/hardware.md).
2. Uruchom [pomiar i kalibrację](docs/commissioning.md) z odłączoną pompą.
3. Po zapisaniu pomiarów przejdź do prób hydraulicznych opisanych w tej samej instrukcji.
4. Zobacz [plan rozwoju](docs/roadmap.md), w tym zakres przyszłego panelu.

`firmware/read_soil.py` to skrypt diagnostyczny uruchamiany ręcznie. Publikuje surowe odczyty przez konsolę USB. Test na docelowym sprzęcie jest jeszcze przed projektem.
