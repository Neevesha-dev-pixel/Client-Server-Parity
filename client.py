import socket
import math
import random
import sys
import os
from PIL import Image
path = '/home/client/Documents/client-server/Photos'
files = os.listdir(path)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 2222))


for x in files:
    print(x)

filename = input("Choose an image : ")
file = open("Photos/" + filename,'rb')
data = file.read(1024)
    
while data:
    client.send(data)
    data = file.read(1024)
	
a = random.randint(0,100)
binary1 = list(map(int, format(a, "b")))

r = 0

while((len(binary1) + r + 1) > pow(2,r)):
    r = r+1

binaryy = [0] * (len(binary1) + r)

j = len(binary1)-1
p = 0

for i in range(0, len(binary1) + r):
    if (pow(2,p) - 1 == i):
        p += 1
    else:
        binaryy[i] = binary1[j]
        j -= 1
parity = []

for j in range(1, r+1):
    list1 = []
    for i in range(1, len(binary1) + r + 1):
        x = format(i, "b")
        if(j <= len(x) and x[0-j] == '1' and binaryy[i-1] == 1):
            list1.append(1)
    if(len(list1)%2 == 0): parity.append(0)
    else: parity.append(1)

j = 0
p = 0
for i in range(0, len(binary1) + r):
    if (pow(2,p) - 1 == i):
        binaryy[i] = parity[j]
        p += 1
        j += 1

binaryy.reverse()
msg = ''.join(str(x) for x in binaryy)
print("Parity bit = " + str(msg))
client.send(bytes(msg,'utf-8'))

file.close()
client.close()

