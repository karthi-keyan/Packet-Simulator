import PacketSimulator
import time

simulator = PacketSimulator.packetSimulatorClient()

simulator.startThread()

while(True):
    print(simulator.dataPacket)
    time.sleep(2)
