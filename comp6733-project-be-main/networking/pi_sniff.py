'''
- This code should be run from the base of the repository (../comp6733-project-be)
- Make sure to set the wifi_interface on the raspberry pi to monitor mode before running this script
'''
import paramiko
import time

'''
TODO: Set these global variables yourself
'''
# These depend on the Raspberry Pi
# Raspberry Pi 1: The one with the red label
HOSTNAME_1 = "172.20.10.9" # hostname of the Raspberry Pi. Should just be the ip address
OUTPUT_FILENAME_1 = "output1.pcap" # name of the tcpdump output file

# Raspberry Pi 2 : The one without a box
HOSTNAME_2 = "172.20.10.4" # hostname of the Raspberry Pi. Should just be the ip address
OUTPUT_FILENAME_2 = "output2.pcap" # name of the tcpdump output file

# Raspberry Pi 3: The one in a box with no red label
HOSTNAME_3 = "172.20.10.5" # hostname of the Raspberry Pi. Should just be the ip address
OUTPUT_FILENAME_3 = "output3.pcap" # name of the tcpdump output file

# These are probably common between all Raspberry Pi's. Add extra global variables if needed
USERNAME = "admin" # username of the Raspberry Pi
PASSWORD = "1c2r$aV3m0n3x#9" # password of the username on the Raspberry Pi
WIFI_INTERFACE = "wlan1" # name of the wifi interface on the Raspberry Pi which we're sniffing from
REMOTE = "/home/admin/" # complete filepath of the output file on the Raspberry Pi
LOCAL = "networking/datafiles/" # filepath of the output file on this machine

'''
HELPER FUNCTION
Creates SSH client for Raspberry Pi indicated by hostname
Returns: client object
'''
def create_client(hostname):
    # Create connection
    client = paramiko.SSHClient()
    # client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # risk for man in the middle attacks. Use only if the line below isn't working
    client.load_system_host_keys() # requires host key to be cached. Might need to run the above line once, or manually ssh into the Pi first
    client.connect(hostname, username=USERNAME, password=PASSWORD)
    return client

'''
HELPER FUNCTION
Copies .pcap file from Raspberry Pi to 'datafiles/' directory and closes SSH client
'''
def copy_close_client(client, output_filename):
    # Copy output file to 'datafiles/' directory
    sftp_client = client.open_sftp()
    sftp_client.get(REMOTE + output_filename, LOCAL + output_filename)
    sftp_client.close()

    # Remove output.pcap on the Raspberry Pi and close the SSH client
    client.exec_command('rm -f ' + output_filename)
    client.close()

'''
CALL THIS FUNCTION FROM OUTSIDE THIS FILE
Commands all three Raspberry Pi sniffers to sniff packets and then transfer the collected .pcap files to the 'datafiles/' directory
'''
def sniff_packets():
    print("Creating remote clients for Pi sniffing!")
    # Create clients
    client1 = create_client(HOSTNAME_1)
    client2 = create_client(HOSTNAME_2)
    client3 = create_client(HOSTNAME_3)

    # Execute command
    print("Running tcpdump on Pi for 3 minutes!")
    client1.exec_command('sudo timeout 2m tcpdump -i ' + WIFI_INTERFACE + ' -w ' + OUTPUT_FILENAME_1 + ' subtype probe-req')
    client2.exec_command('sudo timeout 2m tcpdump -i ' + WIFI_INTERFACE + ' -w ' + OUTPUT_FILENAME_2 + ' subtype probe-req')
    client3.exec_command('sudo timeout 2m tcpdump -i ' + WIFI_INTERFACE + ' -w ' + OUTPUT_FILENAME_3 + ' subtype probe-req')
    time.sleep(125)

    # Copy files and close clients
    print("SFTP-ing .pcap files for Triangulation!")
    copy_close_client(client1, OUTPUT_FILENAME_1)
    copy_close_client(client2, OUTPUT_FILENAME_2)
    copy_close_client(client3, OUTPUT_FILENAME_3)

# if __name__ == "__main__":
#     sniff_packets()
