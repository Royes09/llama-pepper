import socket
from file2 import output_ai

def main () :
    host = '127.0.0.1'
    port = 8888
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = output_ai()
    client_socket.sendall(message.encode())
    client_socket.close()

main()