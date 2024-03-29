import socket
import os
import binascii

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

os.system("sudo fuser -k -n tcp {}".format(10000))

# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            # info = str(binascii.hexlify(data).decode('iso-8859-1')).upper()
            print('Data: {!r}'.format(data))
            # if data:
            #     print('sending data back to the client')
            #     connection.sendall(data)
            # else:
            #     print('no data from', client_address)
            #     break

    finally:
        # Clean up the connection
        connection.close()

