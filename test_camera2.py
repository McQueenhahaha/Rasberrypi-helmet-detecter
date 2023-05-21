from picamera2 import Picamera2, Preview
import time
import cv2
cv2.startWindowThread()
picam = Picamera2()
#camera_config = picam.create_preview_configuration()
#picam.start_preview(Preview.QTGL)
picam.start()
#time.sleep(10)
#picam.capture_file("test.jpeg")
#load and prepare image
while True:
	image = picam.capture_array()
	image = cv2.resize(image,(300,300))
	cv2.imshow("hello",image)
print("done")
