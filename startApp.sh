#!/bin/bash
res=`ss -antp | grep 8001`
if [ ! -z "$res" ]
then
    kill -9 `echo $res | cut -d= -f2 | cut -d, -f1`
fi
gnome-terminal -- /bin/sh -c 'cd /home/karthikeyan/Desktop/Packet-Simulator-master/packetSimulator/; python3 PacketServer.py'
sleep 1
cd /home/karthikeyan/Desktop/Packet-Simulator-master/packetSimulator/
python3 test.py