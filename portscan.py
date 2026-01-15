import socket
import sys

if len(sys.argv)<2:
	print("Host not indicated")
	sys.exit(1)
if len(sys.argv)<3:
	print("Port range not indicated")
	sys.exit(1)
host = sys.argv[1]
for port in range(1,int(sys.argv[2])+1):
	try:
		scanner = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		scanner.settimeout(1)
		result = scanner.connect_ex((host,port))
		if result == 0:
			print(f"port {port} is open")
	except socket.error:
		pass
	finally:
		scanner.close()

