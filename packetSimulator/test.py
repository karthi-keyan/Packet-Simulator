import PacketSimulator
import time
import datetime
from modelSrc import getModel
from packetConvertor import convertPacket
import numpy as np

counter=0
DOS_THREAD_COUNT=0
prev_packet=[]

simulator = PacketSimulator.packetSimulatorClient()

simulator.startThread()

model = getModel()

while(True):
    data=simulator.dataPacket
    if counter>0:
        data=convertPacket(str(data['data']).split(',')[:41])
        if data==prev_packet:
            DOS_THREAD_COUNT+=1
        else:
            prev_packet=data
            DOS_THREAD_COUNT=0
        if data != "ERROR_STATUS":
            inp = np.array(data).reshape(1,-1)
            print("Packet ",counter,"\tTimestamp ",datetime.datetime.now())
            if model.predict(np.array(inp).reshape(1,-1))[0]==1:
                print("Status : No potential thread found")
            else:
                print("Status : Potential thread found")
            if DOS_THREAD_COUNT>10:
                print("Alarm : Predicted DOS Attack thread")
        print("\n")
    counter+=1
    time.sleep(2)
