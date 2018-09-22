import re



def fileSend(sock, payload):
    
    filein = open(payload,"r")
    for l in filein:
        
        msg = l
        while len(msg):
            nsent = sock.send(msg)



def recieveFile(sock):

    fileopen = open("serverText.txt", "w")
    r = sock.recv(100)
    fileopen.write(r)
