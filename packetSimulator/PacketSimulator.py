import socket
from multiprocessing import Process,Manager,Value
from ctypes import c_char_p
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

class packetSimulatorClient:
    
    def __init__(self):
        self.HOST = '127.0.0.1'  
        self.PORT = 8001
        manager = Manager()
        self.dataPacket = manager.dict()
        self.dataPacket["data"] = ""
        self.dataHeader=[]       

    def receivePackets(self,dataPacket_): 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.HOST, self.PORT))
                print("Packet Simulator client connected....")
                data = str(s.recv(1024)).split(",")
                while(True):
                    data = s.recv(1024)
                    if data=="end":
                        print("Packet Data ends....")
                        break
                    else:
                        dataPacket_["data"]=data
            except Exception as e:
                print(e)

    def startThread(self):
        process = Process(target=self.receivePackets,args=(self.dataPacket,))        
        process.start()  
