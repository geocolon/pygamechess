import socket
from _thread import *
import sys
import signal

        #  192.168.1.187 netmask 0xffffff00 broadcast 192.168.1.255

server = "192.168.1.187"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a conncetion, Server Started")


def threaded_client(conn):
    conn.send(str.encode("Connected"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            print(f"Error: {e}")
            break
    print("Lost connection")
    conn.close()

def signal_handler(sig, frame):
    print("\nServer is shutting down gracefullly...")
    s.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
        
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))