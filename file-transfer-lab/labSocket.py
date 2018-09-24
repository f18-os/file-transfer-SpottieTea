import re



def fileSend(sock, payload):
    
    filein = open(payload,"rb")
    lines = filein.readlines()
    for l in lines: #for each line, send over socket
        print(l)
        print("\n")
        msg = l
        nsent = sock.send(msg)



def receiveFile(sock):
    
    fileopen = open("serverText.txt", "w")
    r = sock.recv(100) #receive bytes
    line = r.decode('ascii') #decode bytes
    print(line) #check if recieved
    fileopen.write(line) #write to file
    
