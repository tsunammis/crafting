# Create 2000 connection
python -c 'import socket; [socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("localhost", 80)) for i in range(2000)]'
