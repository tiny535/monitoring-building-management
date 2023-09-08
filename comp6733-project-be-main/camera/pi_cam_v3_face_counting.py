from picamera2 import Picamera2
import cv2
import os

"""
    This code should be run from the base of the repository (../comp6733-project-be)
    This code integrates the PiCamera 3 with the facial recognition code.
    This code capture an image every 3 minutes and counts the number of faces identified in the image.
"""

# Load the pre-trained cascade classifier for face detection
face_classifier = cv2.CascadeClassifier("camera/haarcascade_frontalface_default.xml")

# Initialise the camera
camera = Picamera2()

# Function to draw rectangles around the detected faces
def detect_bounding_box(vid):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    
    # Perform face detection
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)

    return faces

camera.start()

# Capture a frame from the camera
image_path = "/home/singrayr/Desktop/comp6733-project-be/camera/images/photo.jpg"
camera.capture_file(image_path)
video_frame = cv2.imread(image_path)

# Apply the function created to the video frame
faces = detect_bounding_box(video_frame)

# Count the number of faces detected
num_faces = len(faces)

# Display the processed frame (for debugging purposes)
# cv2.imshow("My Face Detection Project", video_frame)

# Print the number of faces detected in the captured image
# print(f"Picture taken: {num_faces} face(s) detected")
print(f"Count: {num_faces}")

# Only used when cv2.imshow() is called
# cv2.destroyAllWindows()

# Check if image_path exists. If so, delete
if os.path.exists(image_path):
    os.remove(image_path)
