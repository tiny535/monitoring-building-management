# comp6733-project

## Setting up Raspberry Pi
1. Follow instructions [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)
2. Follow [this](https://raspberrypi-guide.github.io/networking/connecting-via-ssh) guide for how to set up Raspberry Pi via SSH

### Optional for SSH
You may run into issues when setting up SSH, try running the following command:   
`ssh-keygen -f "/home/singrayr/.ssh/known_hosts" -R "raspberrypi.local"`

This will allow you to SSH without password.

## Set up OpenCV on Raspberry Pi
1. Follow instructions [here](https://littlebirdelectronics.com.au/guides/165/set-up-opencv-on-raspberry-pi-4)

Note: Instead of running `sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev` 

Try running `sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev` instead.

[Solution found here](https://askubuntu.com/questions/991706/e-package-libpng12-dev-has-no-installation-candidate)

## How to take a photo using the USB Camera
1. Follow instructions [here](https://raspberrypi-guide.github.io/electronics/using-usb-webcams)
2. Specificallly `sudo apt install ffmpeg` & `ffmpeg -f v4l2 -video_size 1280x720 -i /dev/video0 -frames 1 out.jpg`

## Testing Facial Recognition based on .jpg (Single faces)
1. Download dataset from [here](http://vis-www.cs.umass.edu/lfw/)
2. Run `facial_recognition.py`
3. Grab a coffee
4. Inspect output

## Testing Facial Recognition based on .jpg (Multiple faces)
1. Download datasets from [here](http://chenlab.ece.cornell.edu/people/Andy/ImagesOfGroups.html)
2. Run `facial_recognition.py`
3. Grab a coffee
4. Inspect output

## Putting the WiFi Interface in monitor mode:
https://www.geeksforgeeks.org/how-to-put-wifi-interface-into-monitor-mode-in-linux/amp/
1. Run `sudo iw dev` to get the name of the WiFi interface.
2. Run the following commands:

`sudo ip link set [WiFi_Interface_Name] down`

`sudo iw [WiFi_Interface_Name] set monitor none`

`sudo ip link set [WiFi_Interface_Name] up`

3. Run `sudo iw dev` again to check that it is in monitor mode.
4. To switch back to managed mode (needed to connect to a network), run the following

`sudo ip link set [WiFi_Interface_Name] down`

`sudo iw [WiFi_Interface_Name] set type managed`

`sudo ip link set [WiFi_Interface_Name] up`

## Sniffing packets
1. If tcpdump is not installed, install using `sudo apt-get install tcpdump`
2. While the WiFi interface is in monitor mode, run `tcpdump -i [WiFi_Interface_Name]`
3. To apply a probe request filter, run `tcpdump -i [WiFi_Interface_Name] subtype probe-req`. Full list of filters can be found here: https://www.tcpdump.org/manpages/pcap-filter.7.html
4. To dump the sniffed packed in a .pcap file, run `tcpdump -i [WiFi_Interface_Name] -w [Filename].pcap subtype probe-req`. Full list of options for tcpdump can be found here: https://linux.die.net/man/8/tcpdump
5. .pcap files can be opened and analysed in Wireshark if desired

## How to run backend
1. Install flask
2. Run `python3 app.py` from `../comp6733-project-be/server`

## How to set up sniffers
1. Run setup_pi.sh using the following commands:

`chmod +x setup_pi.sh`

`sudo ./setup_pi.sh`

2. Connect the Raspberry Pi sniffers and the backend to the same WLAN
3. Find the IP address of each Raspberry Pi using the command `hostname -I`. Alternate methods of finding IP address can be found here: https://www.raspberrypi.com/documentation/computers/remote-access.html
4. In `networking/pi_sniff.py`, set the following parameters:

`HOSTNAME_1 = "[IP_ADDRESS_RP1]"`

`HOSTNAME_2 = "[IP_ADDRESS_RP2]"`

`HOSTNAME_3 = "[IP_ADDRESS_RP3]"`

5. On each Raspberry Pi sniffer, run `sudo ifconfig`. Find the MAC address for the `wlan0` interface. In `networking/triangulate.py`, set the following parameters:

`PI1_WLAN = "[MAC_ADDRESS_RP1]"`

`PI2_WLAN = "[MAC_ADDRESS_RP2]"`

`PI3_WLAN = "[MAC_ADDRESS_RP3]"`
   
6. In `networking/triangulate.py`, set the following parameters with the coordinates of each Raspberry Pi sniffer: `X_1`, `Y_1`, `X_2`, `Y_2`, `X_3`, `Y_3`
7. In `networking/triangulate.py`, set the following parameters with the boundaries of your room: `X_MIN`, `Y_MIN`, `X_MAX`, `Y_MAX`
8. Install `requirements.txt` on backend machine
