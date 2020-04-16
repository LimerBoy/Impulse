import os
import wget
import platform

if platform.system() == "Windows":
	winpcap_url = "https://www.winpcap.org/install/bin/WinPcap_4_1_3.exe"
	winpcap_dir = os.environ["ProgramFiles(x86)"] + "\\WinPcap"
	if not os.path.exists(winpcap_dir):
		print("[!] Attention! Component \"WinPcap\" not installed!\n    is needed to make an attack of tcp, udp and others,\n    you can skip this if you want to use only SMS flood\n    Do you want to install it automatically? (y/n)")
		if input(" >>> ").lower() in ("y", "yes", "1"):
			print("[~] Downloading installer...\n")
			winpcap_installer = wget.download(winpcap_url)
			os.startfile(winpcap_installer)
			print("\n\n[?] Now please restart program")
			exit()
