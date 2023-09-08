import paramiko

"""
    This code should be run from the base of the repository (../comp6733-project-be)
    This code is used on backend machine to remotely call pi_cam_v3_face_counting.py
"""

# Raymonds Personal Pi
HOSTNAME = "172.20.10.8" 
USERNAME = "singrayr" # username of the Raspberry Pi
PASSWORD = "Ramendra32!" # password of the username on the Raspberry Pi
REMOTE = "/home/singrayr/Desktop/comp6733-project-be/camera/usb_cam_face_counting.py" # complete filepath of the output file on the Raspberry Pi

"""
    Creates SSH client for Raspberry Pi indicated by hostname
    Returns: client object
"""
def create_client(hostname):
    # Create connection
    client = paramiko.SSHClient()
    # client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # risk for man in the middle attacks. Use only if the line below isn't working
    client.load_system_host_keys()
    client.connect(hostname, username=USERNAME, password=PASSWORD)
    return client


"""
    CALL THIS FUNCTION FROM OUTSIDE THIS FILE
    Commands Pi which is running camera to check the num of people.
"""

def face_count():
    print("Creating remote clients for Pi face counting!")
    # Create clients
    client = create_client(HOSTNAME)

    # Execute command
    print("Running face counting on Pi!")
    # Read here to understand why I stringed multiple commands together: 
    # https://stackoverflow.com/questions/8932862/how-do-i-change-directories-using-paramiko

    # Read here to understandw why I used python -u: 
    # https://stackoverflow.com/questions/43637325/get-output-of-python-remotely-in-realtime
    stdin, stdout, stderr = client.exec_command('cd /home/singrayr/Desktop/comp6733-project-be; python3 -u camera/usb_cam_face_counting.py')

    result = []
    for line in stdout:
        result.append(line.rstrip())

    client.close()

    # Print the output
    num_people = result[-1].split(":")[1]
    return int(num_people)