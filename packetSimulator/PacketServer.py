import socket
import csv
import time
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

dataToSend = open("Train_data.csv",'r')
dataToSend = csv.reader(dataToSend, delimiter=' ', quotechar='|')

HOST = '127.0.0.1'  
PORT = 8001        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Server Started...")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        for row in dataToSend:
            conn.send(bytes(row[0],encoding="utf-8"))
            time.sleep(1)
        conn.send("end")
