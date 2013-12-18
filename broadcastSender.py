from socket import *

bc = socket(AF_INET, SOCK_DGRAM) # ipv4 UDP

host = '255.255.255.255'
port = 44001

bc.connect((host,port))
data = bytes("BROADCASTTEST", "utf-8")
bc.send(data)