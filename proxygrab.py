import urllib
import re
import os
import time
from colorama import Fore

def print2(msg):
	print Fore.RED + "[*] " + Fore.WHITE + str(msg)
def printProxy(prox):
	print Fore.RED + "[*] " + Fore.BLUE + str(prox)

print2("Buscando proxys...")

page = urllib.urlopen("http://proxy-daily.com/").read()
result = re.findall('\d+\.\d+\.\d+\.\d+\:\d{1,}', page)



if os.path.exists('proxys.txt'):
	os.remove("proxys.txt")

f = open("proxys.txt","w+")


time.sleep(2)

print2(str(len(result)) + " Proxys coletados..")


time.sleep(3)
for proxy in result:
	f.write(str(proxy) + "\n")
	printProxy(proxy)

asci = """
		           ____
		      _,-ddd888888bbb-._
		    d88888888888888888888b
		  d888888888888888888888888b
		 6888888888888888888888888889
		 68888b8""8q8888888p8""8d88889
		 `d8887     p88888q     4888b'
		  `d8887    p88888q    4888b'
		    `d887   p88888q   488b'
		      `d8bod8888888dob8b'
		        `d88888888888d'
		          `d8888888b'
		            `d8888b' 
		              `bd'
		              fsociety tool 
		              		by gusdnide

"""
print(asci)
print2("Salvo em proxys.txt.")

f.close()



