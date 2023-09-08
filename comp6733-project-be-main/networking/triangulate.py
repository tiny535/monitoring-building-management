'''
- Make sure you install libpcap (Unix) or npcap (Windows) before running this script
- This code should be run from the base of the repository (../comp6733-project-be)
'''
from scapy.all import *
import numpy
import os

# Triangulation coefficients. DO NOT CHANGE
M_VAR = -3.298438005258194
C_VAR = -44.696753694096515

'''
TODO: Set these global variables yourself
'''
# Double check these wireless adapters' MAC addresses
PI1_WLAN = "00:e0:4c:04:f4:e2"
PI2_WLAN = "00:e0:4c:04:f7:90"
PI3_WLAN = "00:e0:4c:08:ba:54"

# Set .pcap file names from each of the Raspberry Pi sniffers
PI1_PCAP = "output1.pcap"
PI2_PCAP = "output2.pcap"
PI3_PCAP = "output3.pcap"
LOCAL_PATH = "networking/datafiles/"

# Set the coordinates of each Raspberry Pi
X_1 = 4.8
Y_1 = 9.5

X_2 = 0.6
Y_2 = 9.7

X_3 = 0.7
Y_3 = 0.2

# Set room boundaries. Assuming rectangular room
X_MIN = 0
Y_MIN = 0
X_MAX = 5.4
Y_MAX = 11.3

'''
HELPER FUNCTION
Compiles a list of unique source MAC addresses (src) inside pcap_file.
List contains dictionaries:
{
    'src': source MAC address,
    'rssi': signal strength
}
'''
def filter_packets(pcap_file):
    filtered_list = []
    for pkt in pcap_file:
        # If the packet is not from any of the Raspberry Pi sniffers' wireless adapters
        if (str(pkt.addr2) != PI1_WLAN) and (str(pkt.addr2) != PI2_WLAN) and (str(pkt.addr2) != PI3_WLAN):
            # If the source MAC address is unique, add the packet to the filtered_list
            if not any(p.get('src') == pkt.addr2 for p in filtered_list):
                filtered_list.append({'src': pkt.addr2, 'rssi': pkt.dBm_AntSignal})
            
            # Else, check if this is the best signal strength (i.e. negative value closest to 0)
            else:
                for f in filtered_list:
                    if (f.get('src') == pkt.addr2) and (f.get('rssi') < pkt.dBm_AntSignal):
                        f['rssi'] = pkt.dBm_AntSignal

    return filtered_list

'''
HELPER FUNCTION
Finds common source MAC addresses (src) between l1, l2 and l3.
Returns a list of dictionaries:
{
    'src': source MAC address,
    'rssi_1': signal strength from pi1,
    'rssi_2': signal strength from pi2,
    'rssi_3': signal strength from pi3
}
'''
def intersect_MAC_address(l1, l2, l3):
    l2_mac = set(p["src"] for p in l2)
    l3_mac = set(p["src"] for p in l3)
    combined_list = []

    for data in l1:
        if ((data["src"] in l2_mac) and (data["src"] in l3_mac)):
            combined_list.append({'src': data["src"],
                                  'rssi_1': data["rssi"],
                                  'rssi_2': next(i for i in l2 if i['src'] == data["src"]).get('rssi'),
                                  'rssi_3': next(i for i in l3 if i['src'] == data["src"]).get('rssi')
                                  })
    return combined_list

'''
HELPER FUNCTION
Returns distance using the formula "distance = (RSSI - c) / m"
If RSSI is stronger than C_VAR, then we can assume the distance is 0
'''
def calculate_distance(rssi):
    if rssi > C_VAR:
        return 0
    else:
        return ((rssi - C_VAR) / M_VAR)

'''
HELPER FUNCTION
Uses triangulation to determine whether the device is located within the room of interest
Returns: a list of MAC addresses corresponding to devices located within the room of interest
'''
def triangulate(device_list):
    triangulated_list = []

    A = [[2*(X_3 - X_1), 2*(Y_3 - Y_1)],
         [2*(X_3 - X_2), 2*(Y_3 - Y_2)]]

    for device in device_list:
        # calculate distances based on RSSI
        d1 = calculate_distance(device['rssi_1'])
        d2 = calculate_distance(device['rssi_2'])
        d3 = calculate_distance(device['rssi_3'])

        # solve matrix equation
        b = [(d1**2 - d3**2) - (X_1**2 - X_3**2) - (Y_1**2 - Y_3**2), (d2**2 - d3**2) - (X_2**2 - X_3**2) - (Y_2**2 - Y_3**2)]
        x_device, y_device = numpy.linalg.lstsq(A, b, rcond=None)[0]

        # check if device is located within bounds of room
        if (x_device >= X_MIN) and (x_device <= X_MAX) and (y_device >= Y_MIN) and (y_device <= Y_MAX):
            triangulated_list.append(device['src'])

    return triangulated_list

'''
HELPER FUNCTION
Checks if filename exists in LOCAL_PATH. If so, deletes the file
'''
def remove_files(filename):
    if os.path.exists(LOCAL_PATH + filename):
        os.remove(LOCAL_PATH + filename)

'''
CALL THIS FUNCTION FROM OUTSIDE THIS FILE
Returns the number of unique devices sniffed by all three Raspberry Pi sniffers
'''
def process_packets():
    pi1_filtered = filter_packets(rdpcap(LOCAL_PATH + PI1_PCAP))
    pi2_filtered = filter_packets(rdpcap(LOCAL_PATH + PI2_PCAP))
    pi3_filtered = filter_packets(rdpcap(LOCAL_PATH + PI3_PCAP))
    intersection_list = intersect_MAC_address(pi1_filtered, pi2_filtered, pi3_filtered)
    print(f"Total number of devices captured in tcpdump across 3 Pi's: {len(intersection_list)}")
    triangulated_list = triangulate(intersection_list)

    # Delete .pcap files
    remove_files(PI1_PCAP)
    remove_files(PI2_PCAP)
    remove_files(PI3_PCAP)

    return len(triangulated_list)

# if __name__ == "__main__":
#     process_packets()
