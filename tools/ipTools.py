# Import modules
import sys
import socket
import ipaddress
import requests
from urllib.parse import urlparse
from tools.EMAIL.emailTools import ReadSenderEmail
from time import sleep
from colorama import Fore

""" Check if site is under CloudFlare protection """


def __isCloudFlare(link):
    parsed_uri = urlparse(link)
    domain = "{uri.netloc}".format(uri=parsed_uri)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4").text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for i in range(len(ipv4)):
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ipv4[i]):
                print(
                    f"{Fore.RED}[!] {Fore.YELLOW}The site is protected by CloudFlare, attacks may not produce results.{Fore.RESET}"
                )
                sleep(1)
    except socket.gaierror:
        return False


""" Return ip, port """


def __GetAddressInfo(target):
    try:
        ip = target.split(":")[0]
        port = int(target.split(":")[1])
    except IndexError:
        print(f"{Fore.RED}[!] {Fore.MAGENTA}You must enter ip and port{Fore.RESET}")
        sys.exit(1)
    else:
        return ip, port


""" Return url (for HTTP method) """


def __GetURLInfo(target):
    if not target.startswith("http"):
        target = f"http://{target}"
    return target


""" Get target, subject, body """


def __GetEmailMessage():
    server, username = ReadSenderEmail()
    subject = input(f"{Fore.BLUE}[?] {Fore.MAGENTA}Enter the Subject (leave blank for random value): ")
    body = input(f"{Fore.BLUE}[?] {Fore.MAGENTA}Enter Your Message (leave blank for random value): ")
    return [server, username, subject, body]

""" Return target """


def GetTargetAddress(target, method):
    if method == "SMS":
        if target.startswith("+"):
            target = target[1:]
        return target
    elif method == "EMAIL":
        email = __GetEmailMessage()
        email.append(target)
        return email
    elif method in (
        "SYN",
        "UDP",
        "NTP",
        "POD",
        "MEMCACHED",
        "ICMP",
        "SLOWLORIS",
    ) and target.startswith("http"):
        parsed_uri = urlparse(target)
        domain = "{uri.netloc}".format(uri=parsed_uri)
        origin = socket.gethostbyname(domain)
        __isCloudFlare(domain)
        return origin, 80
    elif method in ("SYN", "UDP", "NTP", "POD", "MEMCACHED", "ICMP", "SLOWLORIS"):
        return __GetAddressInfo(target)
    elif method == "HTTP":
        url = __GetURLInfo(target)
        __isCloudFlare(url)
        return url
    else:
        return target


""" Is connected to internet """


def InternetConnectionCheck():
    try:
        requests.get("https://google.com", timeout=4)
    except:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}Your device is not connected to the Internet{Fore.RESET}"
        )
        sys.exit(1)
