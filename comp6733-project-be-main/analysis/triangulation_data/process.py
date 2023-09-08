from scapy.all import *
import matplotlib.pyplot as plt
import numpy as np

MAC_ADDRESS = "d8:31:cf:9f:3c:ed"

distance = []
rssi = []
for i in range(0, 11):
    filename = 'samsung_' + str(i) + 'm.pcap'
    pcapFile = rdpcap(filename)
    for pkt in pcapFile:
        if (pkt.addr2 == MAC_ADDRESS):
            distance.append(i)
            rssi.append(pkt.dBm_AntSignal)

print(distance)
print(rssi)

x = np.array(distance)
y = np.array(rssi)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print(m)
print(c)

xx = np.linspace(0, 10, 101)
yy = m * xx + c
plt.plot(xx, yy, 'r', label='Fitted line')

plt.scatter(distance, rssi)
plt.xlabel("Distance (m)")
plt.ylabel("RSSI (dBm)")
plt.show()
