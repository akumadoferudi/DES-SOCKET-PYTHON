# socket for server
import socket # library for socket
from _thread import * # library for thread
import sys # library for interaction with local system terminal

from des_generator import generate_key, decrypt, encrypt

# get the host name
host = 'localhost'   # or you can use 'socket.gethostbyname()'
port = 5000
thread_count = 0

# Handling Client
def client_handler(conn):
    conn.send(str.encode('You are now connected to the replay server...', 'utf-8'))
    
    while True:
        data = conn.recv(2048)
        msg = data.decode('utf-8')
        msg_argv = msg.split()
        # check
        # print("msg: ", msg)
        if len(msg_argv) == 1:
            if msg_argv[0] == 'SEEUINHELL!':
                # conn.sendall(str.encode("Server: NAH, I'M GOING TO HEAVEN!", 'utf-8'))
                print("NAH, I'M GOING TO HEAVEN!")
                break
            if KeyboardInterrupt:
                conn.sendall(str.encode("Server: C U IN HELL!", 'utf-8'))
                break
        
        elif len(msg_argv) == 3:
            if msg_argv[0] == 'ENCRYPT!':
                plain_text = msg_argv[1]
                key = msg_argv[2]
                if len(plain_text) == 8 and len(key) == 8:
                    # conn.sendall(str.encode("Server: encrypt {msg_argv[1]} {msg_argv[2]}", 'utf-8'))
                    # print('WOKEEEEEEEEEEEEEEEEEEEEE')
                    # keygen = generate_key(key)
                    plain_message, plain_key, cypher_text = encrypt(plain_text, key)
                    # check
                    # print("Server KEY: " + str.encode(keygen, 'utf-8'))
                    msg = "Server:\nPlain Text: " + str(plain_message) + "\nKey: " + str(plain_key) + "\nCypher text: " + str(cypher_text)
                    conn.sendall(str.encode(msg, 'utf-8'))
                else:
                    conn.sendall(str.encode("Server: message and key must be exact 8 character!", 'utf-8'))
            elif msg_argv[0] == 'DECRYPT!':
                cypher_text = msg_argv[1]
                key = msg_argv[2]
                if len(plain_text) == 8 and len(key) == 8:
                    
                    # check
                    # print("Server KEY: " + str.encode(keygen, 'utf-8'))
                    cypher, plain_key, plain_text = decrypt(cypher_text, key)
                    # check
                    # print("Server KEY: " + str.encode(keygen, 'utf-8'))
                    msg = "Server:\ncypher Text: " + str(cypher) + "\nKey: " + str(plain_key) + "\Plain text: " + str(plain_text)
                    conn.sendall(str.encode(msg, 'utf-8'))
                else:
                    conn.sendall(str.encode("Server: message and key must be exact 8 character!", 'utf-8'))
            else:
                conn.sendall(str.encode("Server: YOU ENTERED THE WRONG COMMAND!", 'utf-8'))
            # reply = f'Server: {msg}'
            # conn.sendall(str.encode(reply, 'utf-8'))
        else:
            conn.sendall(str.encode("Server: YOU ENTERED THE WRONG COMMAND!", 'utf-8'))
    conn.close()
    sys.exit(0)
    
# Accepting Connection
def accept_connections(server_socket):
    Client, address = server_socket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))

# Starting Server
def start_server(host, port):    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((host, port))
    except socket.error as err:
        print(str(err))
    print(f'Server is listing on the port {port}...')
    server_socket.listen()

    while True:
        accept_connections(server_socket)
        
if __name__ == '__main__':
    start_server(host, port)