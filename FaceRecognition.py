
import cv2

# Loads the face recognition classifier
machineFaceRec = cv2.CascadeClassifier(<Add a path to the classifier>\haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread(<Add a path to the image>\images.jpg')

# Convert image to gray color style
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# The function returns a list of rectangles according to the amount of faces that appear in the image
faces = machineFaceRec.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Creating the rectangles on a found face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
