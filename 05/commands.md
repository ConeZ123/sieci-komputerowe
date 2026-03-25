# Podstawowe polecenia sieciowe

## 1. Lista interfejsów sieciowych w systemie w postaci par nazwa-status, np.

```
lo       UNKNOWN
eth0     UP
wlan0    DOWN
```

```

```

## 2. Adres MAC routera, który łączy sieć pracowni z internetem.

```

```

## 3. Zmiana adresu MAC karty sieciowej Ethernet na inną wartość.

```

```

## 4. Ping wszystkich urządzeń jednocześnie w podsieci pracowni.

```
```

## 5. Skan całej podsieci pracowni w poszukiwaniu urządzeń z otwartym portem 22.

```
```

## 6. Skan wszystkich portów, które są otwarte na interfejsie lo (loopback).

```
nmap -p- 127.0.0.1
```

## 7. Porty otwarte w systemie wraz z numerem PID procesu i nazwą programu.

```
```

## 8. Wyświetl trasę domyślną w systemie.

```
ip route
```

## 9. Trasa pakietów, które trafiają do serwera kosmatka.pl.

```
traceroute kosmatka.pl
```

## 10. Adres serwera DNS, który jest ustawiony w systemie operacyjnym.

```
cat /etc/resolv.conf | grep nameserver
```

## 11. Lista statycznych wpisów DNS w systemie.

```
cat /etc/hosts
```

## 12. Rekord DNS poczty e-mail kosmatka.pl korzystając z serwera DNS 8.8.8.8 (bez edycji globalnych ustawień DNS).

```
```

## 13. Adres IPv6 hosta google.pl.

```
nslookup -q=AAAA google.com
```

## 14. Data rejestracji domeny kosmatka.pl i do kiedy jest opłacona.

```
whois kosmatka.pl | grep renewal
```

## 15. Adres strony z listą domen .pl usuniętych dzisiejszego dnia.

```
```