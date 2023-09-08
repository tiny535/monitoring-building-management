import cv2

"""
    This code should be run from the base of the repository (../comp6733-project-be)
    This code is used to control the USB Camera.
    As of now, all this is doing is:
        1. Initalising the camera.
        2. Taking a photo with the camera.
        3. Saving the photo.
"""

# Initialise the camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# Capture a frame from the camera
ret, frame = cap.read()

# Check if the frame was captured successfully
if not ret:
    print("Failed to capture frame")
    exit()

# Save the frame as an image file
cv2.imwrite("/home/singrayr/Desktop/comp6733-project-be/camera/images/photo.jpg", frame)

# Release the camera
cap.release()

# Display a message indicating the successful capture
print("Photo captured successfully")
