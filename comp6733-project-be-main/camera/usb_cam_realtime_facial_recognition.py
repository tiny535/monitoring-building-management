import cv2

"""
    This code should be run from the base of the repository (../comp6733-project-be)
    This code integrates the USB Camera with the facial recognition code.\
    This code detects faces in real-time.
"""

# Load the pre-trained cascade classifier for face detection
face_classifier = cv2.CascadeClassifier("camera/haarcascade_frontalface_default.xml")

# Initialise the camera
video_capture = cv2.VideoCapture(2)

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


while True:
    # Capture a frame from the camera
    result, video_frame = video_capture.read()
    if result is False:
        break  
    
    # Apply the function created to the video frame
    faces = detect_bounding_box(video_frame) 
    
    # Create window with freedom of dimensions
    cv2.namedWindow("My Face Detection Project", cv2.WINDOW_NORMAL)    # Create window with freedom of dimensions
    
    # Resize
    imS = cv2.resize(video_frame, (1920, 1080))

    # Display the processed frame
    cv2.imshow("My Face Detection Project", imS)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()