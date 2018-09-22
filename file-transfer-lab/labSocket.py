import re



def fileSend(sock, payload):
    
    filein = open(payload,"rb")
    for l in filein:
        
        msg = l
        while len(msg):
            nsent = sock.send(msg)



def receiveFile(sock):

    fileopen = open("serverText.txt", "w")
    r = sock.recv(100)
    line = r.decode('ascii')
    print(line)
    fileopen.write(line)
