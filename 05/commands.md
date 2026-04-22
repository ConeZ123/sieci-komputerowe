# Podstawowe polecenia sieciowe

## 1. Lista interfejsów sieciowych w systemie w postaci par nazwa-status, np.

```
lo       UNKNOWN
eth0     UP
wlan0    DOWN
```

```
ip link | awk -F ': ' '{print $2, $3}' | awk '{print $1, $8}'
```

```
lo       UNKNOWN
eth0     UP
```

## 2. Adres MAC routera, który łączy sieć pracowni z internetem.

```
ip route | grep default
arp -n 192.168.64.1
```

```
default via 192.168.64.1 dev eth0 proto dhcp src 192.168.64.6 metric 100

Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.64.1             ether   a2:9a:8e:68:f6:64   C                     eth0

```

## 3. Zmiana adresu MAC karty sieciowej Ethernet na inną wartość.

```
sudo ip link set dev eth0 down
sudo ip link set dev eth0 address 02:11:22:33:44:55
sudo ip link set dev eth0 down
```

```
link/ether 02:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff permaddr ee:cf:df:37:d2:ab
```

## 4. Ping wszystkich urządzeń jednocześnie w podsieci pracowni.

```
nmap -sn 192.168.64.0/24
```

```
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-01 17:36 CEST
Nmap scan report for 192.168.64.1
Host is up (0.00048s latency).
MAC Address: A2:9A:8E:68:F6:64 (Unknown)
Nmap scan report for 192.168.64.6
Host is up.
Nmap done: 256 IP addresses (2 hosts up) scanned in 2.33 seconds
```

## 5. Skan całej podsieci pracowni w poszukiwaniu urządzeń z otwartym portem 22.

```
nmap -p 22 192.168.64.0/24
```

```
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-01 17:38 CEST
Nmap scan report for 192.168.64.1
Host is up (0.00049s latency).

PORT   STATE  SERVICE
22/tcp closed ssh
MAC Address: A2:9A:8E:68:F6:64 (Unknown)

Nmap scan report for 192.168.64.6
Host is up (0.000069s latency).

PORT   STATE  SERVICE
22/tcp closed ssh

Nmap done: 256 IP addresses (2 hosts up) scanned in 2.12 seconds
```

## 6. Skan wszystkich portów, które są otwarte na interfejsie lo (loopback).

```
nmap -p- 127.0.0.1
```

```
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-01 16:40 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00s latency).
Not shown: 65533 closed tcp ports (reset)
PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 0.26 seconds
```

## 7. Porty otwarte w systemie wraz z numerem PID procesu i nazwą programu.

```
sudo ss -tulpn
```

```
Netid  State   Recv-Q  Send-Q   Local Address:Port     Peer Address:Port  Process
tcp    LISTEN  0       50             0.0.0.0:139           0.0.0.0:*      users:(("smbd",pid=639,fd=30))
tcp    LISTEN  0       50             0.0.0.0:445           0.0.0.0:*      users:(("smbd",pid=639,fd=29))
tcp    LISTEN  0       50                [::]:139              [::]:*      users:(("smbd",pid=639,fd=28))
tcp    LISTEN  0       50                [::]:445              [::]:*      users:(("smbd",pid=639,fd=27))
```

## 8. Wyświetl trasę domyślną w systemie.

```
ip route
```

```
192.168.64.0/24 dev eth0 proto kernel scope link src 192.168.64.6 metric 100
```

## 9. Trasa pakietów, które trafiają do serwera kosmatka.pl.

```
traceroute kosmatka.pl
```

```
traceroute to kosmatka.pl (217.28.148.190), 30 hops max, 60 byte packets
 1  192.168.64.1 (192.168.64.1)  0.880 ms *  0.708 ms
 2  TUF-BE3600-73B8 (192.168.50.1)  3.804 ms  3.786 ms  3.771 ms
 3  83-238-252-81.static.inetia.pl (83.238.252.81)  9.081 ms  9.067 ms  9.054 ms
 4  warsh002rt22.inetia.pl (83.238.113.56)  10.551 ms  10.536 ms  10.502 ms
 5  100.95.8.3 (100.95.8.3)  10.472 ms  10.417 ms  10.399 ms
 6  100.95.8.0 (100.95.8.0)  10.386 ms  21.603 ms  21.536 ms
 7  83-238-113-57.static.inetia.pl (83.238.113.57)  7.690 ms  7.620 ms  7.601 ms
 8  * * *
 9  * * *
 ...
```

## 10. Adres serwera DNS, który jest ustawiony w systemie operacyjnym.

```
cat /etc/resolv.conf | grep nameserver
```

```
nameserver 192.168.64.1
nameserver fe80::a09a:8eff:fe68:f664%eth0
```

## 11. Lista statycznych wpisów DNS w systemie.

```
cat /etc/hosts
```

```
127.0.0.1       localhost
127.0.1.1       kali

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

## 12. Rekord DNS poczty e-mail kosmatka.pl korzystając z serwera DNS 8.8.8.8 (bez edycji globalnych ustawień DNS).

```
dig @8.8.8.8 kosmatka.pl MX +short
```

```
10 mx2.privateemail.com.
10 mx1.privateemail.com.
```

## 13. Adres IPv6 hosta google.pl.

```
nslookup -q=AAAA google.com
```

```
Server:         192.168.64.1
Address:        192.168.64.1#53

Non-authoritative answer:
Name:   google.com
Address: 2a00:1450:4025:802::66
Name:   google.com
Address: 2a00:1450:4025:802::71
Name:   google.com
Address: 2a00:1450:4025:802::65
Name:   google.com
Address: 2a00:1450:4025:802::8a
```

## 14. Data rejestracji domeny kosmatka.pl i do kiedy jest opłacona.

```
whois kosmatka.pl | grep -E "created|renewal"
```

```
created:                        2022.12.02 12:27:10
renewal date:                   2032.12.02 12:27:10
```

## 15. Adres strony z listą domen .pl usuniętych dzisiejszego dnia.

```
https://www.dns.pl/deleted_domains.txt
```

```
2026-04-01 08:12:07 MEST

0ffice.pl
0x90.pl
101mc.pl
10illusions.pl
120002.pl
123dostawca.pl
12tree.pl
1do.pl
...
```