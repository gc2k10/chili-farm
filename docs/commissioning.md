# Uruchomienie prototypu

## 1. Odczyt czujnika przez USB

Wgraj MicroPython przeznaczony dla Pico 2 W. Na czas pierwszej próby odłącz GFX Pack i obwód pompy. Przy odłączonym USB podłącz czujnik. W prototypie przyjęto GP26 / ADC0. Zweryfikuj oznaczenia przewodów z dokumentacją swojej wersji SEN0193. Przed podaniem sygnału na ADC sprawdź, czy jego napięcie mieści się w zakresie wejścia.

| SEN0193 | Pico 2 W |
| --- | --- |
| VCC | 3V3(OUT) |
| GND | GND |
| AOUT | GP26 / ADC0 |

Podłącz Pico przez USB i uruchom [read_soil.py](../firmware/read_soil.py) w Thonny. Konsola pokaże jedną wartość po uśrednieniu pięciu próbek. Na tym etapie uruchamiaj skrypt ręcznie z edytora.

## 2. Kalibracja dla doniczki

1. Umieść sondę w reprezentatywnym miejscu i zapisz jej położenie. Nie zalewaj elektroniki czujnika.
2. Zapisz serię odczytów w podłożu o wilgotności, przy której normalnie rozważasz podlewanie.
3. Podlej ręcznie, poczekaj na rozprowadzenie wody i odsączenie nadmiaru. Zapisz drugą serię.
4. Powtórz pomiar w kolejnych cyklach. Porównaj kierunek zmian i rozrzut wyników. Wartość ADC zależy od sondy, podłoża i miejsca pomiaru.
5. Zachowaj oba zakresy oraz opis warunków w [dzienniku pomiarów](../examples/soil-log.csv).

## 3. Próba pompki poza doniczką

Przymocuj wężyki i skieruj wylot do naczynia z podziałką. Zmierz objętość dla kilku krótkich prób. Po wyłączeniu sprawdź, czy woda nadal płynie syfonem. Przed próbą automatyczną sprawdź działanie pływaka w stanie pełnym, pustym i przy odpiętym przewodzie. Sprawdź też, czy po restarcie kontrolera pompa pozostaje wyłączona.

Pierwsze próby automatyki wykonuj pod nadzorem. Ustal maksymalny czas pojedynczej dawki oraz odstęp na rozprowadzenie wody na podstawie zmierzonego przepływu i reakcji konkretnego podłoża.
