## Adres sieci

`192.168.0.0/23`

## Zapotrzebowanie na hosty

```
| Podsiec | liczba hostow |    over-provisioning    |
|---------|---------------|-------------------------|
|    1    |      50       |            76           |
|    2    |      30       |            46           |
|    3    |      20       |            31           |
|    4    |      10       |            16           |
|    5    |       5       |             9           |
```

## Dobór masek

```
| Podsiec | Wymagane hosty  | Maska |
|---------|-----------------|-------|
|    1    |       76        |  /25  |
|    2    |       46        |  /26  |
|    3    |       31        |  /26  |
|    4    |       16        |  /27  |
|    5    |        9        |  /28  |
```

## Szegółowa lista podsieci

**Podsiec 1:** <br>
Adres sieci: `192.168.0.0/25` <br>
Pierwszy host: `192.168.0.1` <br>
Ostatni host: `192.168.0.126` <br>
Adres Broadcast: `192.168.0.127` <br>
Liczba hostów: `126` <br>
Nadwyzki:
- względem minimanej: `126 - 50 = 76`
- względem over-provisioningu: `126 - 76: 50`

**Podsiec 2:** <br>
Adres sieci: `192.168.0.128/26` <br>
Pierwszy host: `192.168.0.129` <br>
Ostatni host: `192.168.0.190` <br>
Adres broadcast: `192.168.0.191` <br>
Liczba hostów: `62` <br>
Nadwyzki:
- względem minimanej: `62 - 30 = 32`
- względem over-provisioningu: `62 - 46 = 16`

**Podsiec 3:** <br>
Adres sieci: `192.168.0.192/26` <br>
Pierwszy host: `192.168.0.193` <br>
Ostatni host: `192.168.0.254` <br>
Adres Broadcast: `192.168.0.255` <br>
Liczba hostów: `62` <br>
Nadwyzki:
- względem minimanej: `62 - 30 = 32`
- względem over-provisioningu: `62 - 31 = 31`

**Podsiec 4:** <br>
Adres sieci: `192.168.1.0/27` <br>
Pierwszy host: `192.168.1.1` <br>
Ostatni host: `192.168.1.30` <br>
Adres Broadcast: `192.168.1.31` <br>
Liczba hostów: `30` <br>
Nadwyzki:
- względem minimanej: `30 - 10 = 20`
- względem over-provisioningu: `30 - 16 = 14`

**Podsiec 5:** <br>
Adres sieci: `192.168.1.32/28` <br>
Pierwszy host: `192.168.1.33` <br>
Ostatni host: `192.168.1.46` <br>
Adres Broadcast: `192.168.1.47` <br>
Liczba hostów: `14` <br>
Nadwyzki:
- względem minimanej: `14 - 5 = 9`
- względem over-provisioningu: `14 - 9 = 5`

## Drzewko podziału podsieci 

```
192.168.0.0/23:
    - 192.168.0.0/24: 
        - 192.168.0.0/25: (Podsiec 1, 126)
        - 192.168.0.128/25:
            - 192.168.0.128/26: (Podsiec 2, 62)
            - 192.168.0.192/26: (Podsiec 3, 62)
    - 192.168.1.0/24:
        - 192.168.1.0/27 (Podsiec 4, 30)
        - 192.168.1.32/28 (Podsiec 5, 14)
        - 192.168.1.48/28 (unused 14)
            - 512 - (128 + 64 + 64 + 32 + 16 + 16) = 512 - 320 = 192 wolne adresy
```