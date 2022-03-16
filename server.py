import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 2222
ADDR = (IP, PORT)
FORMAT= "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("SERVER IS LISTENING")

while True:
    conn, add = server.accept()
    print("Connection established with {}".format(add))

    file = open("Downloads/image.jpeg",'wb')    
    filename = conn.recv(1024)
    
    while filename:
        file.write(filename)
        filename = conn.recv(1024)
    
    arr = list(filename)
    arr = list(map(int, arr))
    arr.reverse()
    ansParity = []

    r = 0
    while((len(arr) + 1) > pow(2,r)):
        r = r+1

    for j in range(1, r+1):
        sum = 0
        for i in range(1, len(arr)+1):
            x = format(i, "b")
            if(j <= len(x) and x[0-j] == '1'):
                sum += arr[i-1]

        if(sum%2 == 0): ansParity.append(0)
        else: ansParity.append(1)

    ansParity.reverse()
    print(ansParity)
    tempString = ''.join(str(x) for x in ansParity)
    num = len(tempString)
   
    if(num == 0):
        print("NO ERROR ")
        conn.send(bytes("NO ERROR", FORMAT))
    else:
        print("ERROR at POSITION => " + str(num))
        conn.send(bytes("ERROR at POSITION => " + str(num), FORMAT))
    file.close()
    conn.close()

