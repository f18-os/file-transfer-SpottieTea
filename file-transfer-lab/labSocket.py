import re



def framedSend(sock, payload, debug=0):
    if debug: print("framedSend: sending %d byte message" % len(payload))
    filein = open(payload,"r")
    for l in filein:
        
        msg = str(len(l)).encode() + b':' + l
        while len(msg):
            nsent = sock.send(msg)
            msg = msg[nsent:]



rbuf = b""                      # static receive buffer
