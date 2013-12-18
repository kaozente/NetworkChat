from socket import *

rc = socket(AF_INET, SOCK_DGRAM)

rc.bind(('0.0.0.0', 44001))

print("Listening:")
data, addr = rc.recvfrom(1024)


print(addr)
print(data)