from picamera2 import Picamera2, Preview

"""
    This code should be run from the base of the repository (../comp6733-project-be)
    This code is used to control the PiCamera 3
    As of now, all this is doing is:
        1. Initalising the camera.
        2. Taking a photo with the camera.
        3. Saving the photo.
"""

try:
    # Initialise the camera
    picam2 = Picamera2()

    # Capture a frame from the camera
    picam2.start()

    # Save the frame from the camera
    picam2.capture_file("/home/singrayr/Desktop/comp6733-project-be/camera/images/photo.jpg")

    picam2.stop()

    print("Photo captured successfully")
except Exception as e:
    print("Failed to capture photo: ", str(e))