# for client

import socket
import sys

host = 'localhost'
port = 5000

def start_server(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Waiting for connection')
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(str(e))
    Response = client_socket.recv(2048)
    while True:
        
        plain_text = None
        key = None
        print('''
              Implementatioon of Data Encryption Standard
              If you wanna encrypt a message, type this: 'ENCRYPT! [your 8 char message] [your 8 char key]'
              If you wanna decrypt a message, type this: 'DECRYPT! [your 8 char message] [your 8 char key]'
              ''')
        Input = input('What you gonna do? => ')
        
        # # For Quit the Program
        if Input == 'SEEUINHELL!':
            print("NAH, I'M GOING TO HEAVEN!")
            break
        
        # For Encryption
        else:
            client_socket.send(str.encode(Input))
            Response = client_socket.recv(2048)
            print(Response.decode('utf-8'))
            
            
            # if sys.argv[0] == 'ENCRYPT!':
            #     plain_text = sys.argv[1]
            #     key = sys.argv[2]
            #     if len(plain_text) != 8 and len(key) != 8:
            #         print('you can only input 8 character message and 8 character key!')
            #     else:
            #         print('your message is encrypted!') # for test
            #         client_socket.send(str.encode(Input))
            #         # encode_message(plain_text, key)
            # else:
            #     print('wrong input!')
        
        # For Decryption
        
    client_socket.close()
    sys.exit(0)

    
if __name__ == '__main__':
    start_server(host, port)