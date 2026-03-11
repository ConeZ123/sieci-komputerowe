import sys

def ip_to_int(ip_str: str) -> int:
    a, b, c, d = ip_str.split(".")
    a, b, c, d = int(a), int(b), int(c), int(d)

    return (a >> 24, b >> 16, c >> 8, d)

def int_to_ip(ip: int) -> str:
    ...

def int_to_bin(ip: int):
    return format(ip, "032b")

def network_address(ip: int, mask: int) -> int:
    return ip & mask

def subnet_mask(mask_len: int):
    ...

def first_host(network_address: int) -> int:
    return network_address + 1

def broadcast_address(network_address: int, mask: int) -> int:
    return network_address | ~mask

def last_host(broadcast_address: int) -> int:
    return broadcast_address - 1

def host_number(mask_length: int) -> int:
    return (2 ** (32 - mask_length))

def main():
    arg = sys.argv[1]
    ip_part, mask_part = arg.split("/")
    mask_len = int(mask_part)

