import cv2
import os

"""
    This code should be run from the base of the repository (../comp6733-project-be)
    This code is used to spot-check and bulk test the facial recognition code.
    face_cascade can be changed to any of the .xml files which are located in "camera" directory.
    The "camera/images" directory is used for spot checks.
    The "camera/test" is used for bulk testing. Redirect this output for analysis once test is complete.
    The "camera/test/crowd_2a is a dataset of groups of people.
    The "camera/test/crowd_5a is a dataset of groups of people.
    lbpcascade_frontalface_improved.xml
    haarcascade_frontalface_default.xml
"""

# Load the pre-trained cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('camera/lbpcascade_frontalface_improved.xml')

# Specify the path to the directory containing the images
# Use 'images' by default BUT use 'test' for testing.
image_directory = 'camera/test'

# Loop through each image in the directory
for filename in os.listdir(image_directory):
    # Check the filename ends with .jpg or .png
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image
        image_path = os.path.join(image_directory, filename)

        image = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)

        # # Count the number of faces detected -- Was used when testing crowd facial recognition
        # num_faces = len(faces)
        # print(f"{filename},{num_faces}")

        # Check if a face is detected -- Was used when testing real-time facial detection
        face_detected = len(faces) > 0
        print(f"Face detected in {filename}: {face_detected}")

        # Display the output image        
        if image_directory == 'camera/images':
            # Create window with freedom of dimensions
            cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
            
            # Resize image   
            imS = cv2.resize(image, (1920, 1080))   
            
            # Show image             
            cv2.imshow("output", imS)
            cv2.waitKey(0)

        # Continue along (bulk testing)
        elif 'camera/test' in image_directory:                       
            cv2.waitKey(1)

# Close all windows
cv2.destroyAllWindows()
