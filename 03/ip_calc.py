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

def int_to_bin(ip: int):
    return format(ip, "032b")

def network_address(ip, mask):
    return ip & mask

def subnet_mask(mask_len: int) -> int:
    return (0xffffffff << (32 - mask_len)) & 0xffffffff

def first_host(network_address: int) -> int:
    return network_address + 1

def broadcast_address(network_address: int, mask: int) -> int:
    return network_address | (~mask & 0xffffffff)

def last_host(broadcast_address: int) -> int:
    return broadcast_address - 1

def host_number(mask_length: int) -> int:
    return (2 ** (32 - mask_length)) - 2

def main():
    arg = sys.argv[1]

    ip_part, mask_part = arg.split("/")
    mask_len = int(mask_part)

    ip = ip_to_int(ip_part)
    mask = subnet_mask(mask_len)
    network = network_address(ip, mask)
    broadcast = broadcast_address(network, mask)

    first = first_host(network)
    last = last_host(broadcast)
    hosts = host_number(mask_len)

    print("Adres sieci:")
    print(int_to_ip(network))
    print(int_to_bin(network))

    print("\nMaska podsieci:")
    print(int_to_ip(mask))
    print(int_to_bin(mask))

    print("\nBroadcast:")
    print(int_to_ip(broadcast))
    print(int_to_bin(broadcast))

    print("\nPierwszy host:")
    print(int_to_ip(first))
    print(int_to_bin(first))

    print("\nOstatni host:")
    print(int_to_ip(last))
    print(int_to_bin(last))

    print("\nLiczba hostów:")
    print(hosts)

if __name__ == "__main__":
    main()
