import cv2
import time
camera = cv2.VideoCapture(0)
time.sleep(5)
while True:
	_, frame = camera.read()
	print(frame)
	cv2.imshow("hello",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
camera.release()
cv2.destroyAllWindows() 
