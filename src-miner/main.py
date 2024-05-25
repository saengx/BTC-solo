import os
import json
import time
import pip
from config import banner


# check import module
#try:
#    with open("setip/ip.json", encoding="utf-8") as set:
#            load = set.read()
#            loads = json.loads(load)
#            ip = loads['ip']

#    os.system(f"cd set-miner && wget -N --timeout 5 --connect-timeout=10 -t 1 http://{ip}/online.json")
#    time.sleep(2)
#    from progress.bar import ShadyBar
#except ImportError:
#    pip.main(['install', '--user', 'progress'])
#    from progress.bar import ShadyBar

#try:
#    import requests
#except ImportError:
#    pip.main(['install', '--user', 'requests'])
 #   import requests
    
       
    
def runOffline():
    banner()
    try:
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            password = loads['pass']
        if pool == "" or wallet == "":
            print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit\033[0m\n\n")

        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            name = loads['name']
            cpu = loads['cpu']
        if name == "":
           name = "noname"
        if cpu == "":
           cpu = "1"
        

        print("\033[1;32;40m")   
        print("WALLET =",wallet)
        print("NAME   =",name)
        print("POOL   =",pool)
        print("CPU    =",cpu)
        print("PASS   =",password)
        print("\033[00m\n")

        # time.sleep(2)
         os.system(f"cd miner && ./cpuminer -a sha256d -o {pool} -u {wallet}.{name} -p {password} -t {cpu}")
    except:
        push = {'pool': '','wallet': '','pass': ''}
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)
        push = {'name': '','cpu': ''}
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)
        
        
        
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit\033[0m\n\n")




while True:   
    os.system("@cls||clear")
    with ShadyBar("\033[36m Start Mining\033[00m") as bar:
        for i in range(100):
            time.sleep(0.02)
            bar.next()
            
        runOffline()
        break
else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า กรุณาตั้งค่าโดยใช้คำสั่ง edit\033[0m\n\n")
