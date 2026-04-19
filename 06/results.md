## 1. Adres MAC i IP serwera oraz numer portu TCP, do którego łączy się klient:
```
MAC: 52:34:7f:f0:12:d0
IP: 10.0.1.3
PORT: 7373
```

## 2. Treść wszystkich danych przesyłanych od klienta do serwera (tcp.pcap) w formacie ASCII:
```
8b2c2652b46b20cf0b984439ec3e54a6543a2cb3
x
Y100
Q0
M0
Z0
T87500
A0
F-1
W0
D0
G01
A3
G11
F0
W55000
Z1
X
```

## 3. Zawartość najdłuższego pakietu przesłanego z serwera do klienta (HEX + ASCII dump):
```
0000   7a 9b 67 94 85 b5 52 34 7f f0 12 d0 08 00 45 00   z.g...R4......E.
0010   00 77 94 68 40 00 40 06 91 0c 0a 00 01 03 0a 00   .w.h@.@.........
0020   00 0a 1c cd b8 c4 71 b1 ae 40 bf 9c b3 9f 80 18   ......q..@......
0030   01 fe 93 92 00 00 01 01 08 0a dd 15 f5 34 29 2f   .............4)/
0040   10 fa 4d 30 0a 54 36 34 30 30 30 2c 31 30 0a 5a   ..M0.T64000,10.Z
0050   30 0a 53 6d 2d 30 2e 37 35 2c 39 35 2c 2d 31 0a   0.Sm-0.75,95,-1.
0060   54 38 37 35 30 30 2c 31 30 0a 41 30 0a 57 30 0a   T87500,10.A0.W0.
0070   44 30 0a 47 30 31 0a 53 6d 32 2e 38 32 2c 31 30   D0.G01.Sm2.82,10
0080   30 2c 2d 31 0a                                    0,-1.
```

## 4. Filtr na wszystkie ramki (frame), które zawierają w sobie string ASCII “ok” (case insensitive):
```
frame matches "(?i)ok"
```

## 5. Filtr na pakiet IP z adresu źródłowego 10.0.1.3 i długości payloadu TCP o wartości 13:
```
ip.src == 10.0.1.3 && tcp.len == 13
```
<hr>
<br>
<br>

## 6. Filtr na pakiety ARP Reply lub Ping Reply:
```
arp.opcode == 2 or icmp.opcode == 0
```
## 7. Payload protokołu DNS (bez niższych warstw) z zapytaniem kosmatka.pl w postaci zdekodowanego drzewa:
```
Domain Name System (query)
    Transaction ID: 0xa44c
    Flags: 0x0100 Standard query
    Questions: 1
    Answer RRs: 0
    Authority RRs: 0
    Additional RRs: 0
    Queries
        kosmatka.pl: type HTTPS, class IN
            Name: kosmatka.pl
            [Name Length: 11]
            [Label Count: 2]
            Type: HTTPS (65) (HTTPS Specific Service Endpoints)
            Class: IN (0x0001)
    [Response In: 999]
```
## 8.Zapytanie HTTP do serwera http://mm.kosmatka.pl/ oraz odpowiedź (tylko nagłówki) w formacie ASCII:
```
GET /success.txt?ipv4 HTTP/1.1
Host: detectportal.firefox.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Priority: u=4
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 200 OK
Server: nginx
Content-Length: 8
Via: 1.1 google
Date: Sat, 18 Apr 2026 20:15:36 GMT
Age: 83552
Content-Type: text/plain
Cache-Control: public,must-revalidate,max-age=0,s-maxage=3600
```
## 9. Sposób zapisu obrazka http://mm.kosmatka.pl/favicon.png z Wireshark oraz jego treść w formacie base64:
```
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBI
WXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3wQGABsCuG9X8AAAAB1pVFh0Q29tbWVudAAAAAAAQ3Jl
YXRlZCB3aXRoIEdJTVBkLmUHAAABgElEQVQ4y52Tv0tCURTHP6+ePWxJigThCUKEgzk01BgPEpxs
aqhNWmwJHtRa+AdkODVJ+QdIBM3im5RqEXTRkJbgLZZDEDwSb8N7/nwS1oHLvdxz7+d77jn3ACiA
6sz/srXUybm4vjNFr9cTM1mpJEShIADmAOXdbNLtfmPUZpQ0DGi36QOQpB67kU+MOmMQo4Ybahjg
80EqBYA86ksfwtktPL3A9joUyvZ+9RX0PedQowHB4OCOPBld5gjMD7i8B/8S7EQm1MNh0LTB1ty0
JwaWbdDFAWhRMOo2lHzedVaemqC+OUrahh1RJhQaU3dHMHoZIJ22AVFIeKokrWOX3hBQLEK1aiv0
h88H2awN+XokGfe4qjIECAG6Pu7VdfB6wTShUkHTVlylHgJisemfptmEchmSSQBScXh4/i2Jrrpm
7AgCgUGFEltwejMCsCyLVquFEAJJkqaDOp3B0j8P+5uLXIEiA5aiKORyORRl9oZUVRVgVXLaOAgs
/LGLLeDtB4jwnjHllMVCAAAAAElFTkSuQmCC    
```
Aby sprawdzić, czy obrazek jest poprawny, wklej go do adresu w przeglądarce (Firefox), doklejając na początku: data:image/png;base64,

## 10. Polecenie `tcpdump` do nasłuchu pakietów na interfejsie karty sieciowej wraz z zapisem do pliku output.pcap:
```
tcpdump -i eth0 -w output.pcap
```
