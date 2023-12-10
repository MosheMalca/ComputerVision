
import cv2


machineFaceRec = cv2.CascadeClassifier(r'C:\Users\Moshe\Desktop\studi\computers\projects\ComputerVision\haarcascade_frontalface_default.xml')


img = cv2.imread(r'C:\Users\Moshe\Desktop\studi\computers\projects\ComputerVision\images.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = machineFaceRec.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
