from networking.triangulate import process_packets
from networking.pi_sniff import sniff_packets
from camera.face_count import face_count
import math

def reconcilation():
    sniff_packets()
    num_devices = process_packets()
    num_people = face_count()

    print(f"This is the number of devices counted post-triangulation: {num_devices}")
    print(f"This is the number of faces counted: {num_people}")
    
    reconciled_output = (int(num_devices) + int(num_people)) / 2
    reconciled_output = math.ceil(reconciled_output)

    print(f"This is the reconciled output: {reconciled_output}")
    
    return reconciled_output

