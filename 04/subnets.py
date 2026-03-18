# siec: 192.168.240.0/23
# +1. Siec dla gosci - 100 urzadzen: 100 * 1.5 + 1 = 151
# IT - 50 urzadzen: 50 * 1.5 + 1 = min. 76
# HR - 12 urzadzen: 12 * 1.5 + 1 = 19
# Ksiegowosc - 10 urzadzen: 10 * 1.5 + 1 = 16

import sys

def ip_to_int(ip_str: str) -> int:
    a, b, c, d = ip_str.split(".")
    return (int(a) << 24 | int(b) << 16 | int(c) << 8 | int(d))

def int_to_ip(ip: int) -> str:
    a = (ip >> 24) & 255
    b = (ip >> 16) & 255
    c = (ip >> 8) & 255
    d = ip & 255

    return f"{a}.{b}.{c}.{d}"

def subnet_mask(mask_len: int) -> int:
    return (0xffffffff << (32 - mask_len)) & 0xffffffff

def broadcast_address(network_address: int, mask: int) -> int:
    return network_address | (~mask & 0xffffffff)

def required_hosts(n: int) -> int:
    return (n * 1.5) + 1 

def new_mask(hosts: int) -> int:
    b = 0
    while (2 ** b - 2) > hosts:
        b += 1
    return 32 - b

def main():
    ip_part, mask_part = sys.argv[1].split("/")
    base_ip = ip_to_int(ip_part)

    departments = [
        ("goscie", 100),
        ("IT", 50),
        ("HR", 12),
        ("ksiegowosc", 10),
    ]

