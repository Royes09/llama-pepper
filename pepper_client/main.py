import socket
import naoqi
from naoqi import ALProxy
import os

def main (): 
    host = "127.0.0.1"
    port = 8888
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    os.system("python3 ./Pepper_Server/main.py")
    client_socket, client_address = server_socket.accept()
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        ip_peper = "192.168.1.164"
        tts = ALProxy("ALTextToSpeech", ip_peper, 9559)
        tts.say(data)
    client_socket.close()