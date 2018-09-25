import re



def fileSend(sock, payload):

    #nsent = sock.send(payload.encode())
    filein = open(payload,"rb")
    
    lines = filein.readlines()
    for l in lines: #for each line, send over socket
        print(l)
        msg = l
        nsent = sock.send(msg)



def receiveFile(sock):

    r = sock.recv(100)
    line = r.decode('ascii')
    fileopen = open("serverText.txt","w")
    fileopen.write(line)
    r = sock.recv(100)
    
    while r:
        line = r.decode('ascii') #decode bytes
        print(line) #check if recieved
        fileopen.write(line) #write to file
        r = sock.recv(100)

    
    
