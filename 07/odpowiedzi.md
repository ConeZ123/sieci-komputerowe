## Polecenie instalacji serwera DHCP:
```
sudo apt update
sudo apt install isc-dhcp-server
```

## Konfiguracja interfejsu sieciowego:

```
a. sudo ip link set eth1 down
b. sudo ip addr add 10.123.74.1/24 dev eth1
c. sudo ip link set eth1 up
d. sudo ip route add default via 10.123.74.254
e. echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

## Konfiguracja serwera DHCP (plik conf):
```
subnet 10.123.74.0 netmask 255.255.255.0 {
    range 10.123.74.100 10.123.74.200;
    option routers 10.123.74.1;
    option domain-name-servers 1.1.1.1;
}
```

## Polecenie do uruchomienia serwera DHCP przez systemd:
```
sudo systemctl start isc-dhcp-server
```

## Polecenie do wypisania logów serwera DHCP:
```
journalctl -u isc-dhcp-server
```

## Polecenia do sprawdzenia przydzielonych adresów na komputerze klienckim:
```
ip a
```

## Filtr pakietów DHCP Discover (Wireshark):
```
dhcp.option.dhcp == 1
```

## Filtr pakietów DHCP Offer (Wireshark):
```
dhcp.option.dhcp == 2
```

## Filtr pakietów DHCP Request (Wireshark):
```
dhcp.option.dhcp == 3
```

## Filtr pakietów DHCP ACK (Wireshark):
```
dhcp.option.dhcp == 5
```

## Adres IP przydzielony przed zmianą MAC:
```
10.123.74.100
```

## Adres IP przydzielony po zmianie MAC:
```
10.123.74.101
```