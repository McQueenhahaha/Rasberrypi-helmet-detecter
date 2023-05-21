import cv2
import tflite_runtime.interpreter as tflite
import numpy as np

image_path="helmet.jpg"
image_path="no_helmet.jpg"

#load the tensor lite model
interpreter=tflite.Interpreter(model_path="helmet.tflite")

#allocate memory for the model input
interpreter.allocate_tensors()

#get the input and the output
input_details=interpreter.get_input_details()
output_details=interpreter.get_output_details()

#see the input details
input_shape=input_details[0]["shape"]
print(input_shape)

#load and prepare image
image = cv2.imread(image_path)
image = cv2.resize(image,(300,300))
image = np.expand_dims(image,axis=0).astype(np.uint8)


#start tensor
interpreter.set_tensor(input_details[0]["index"],image)
interpreter.invoke()
prediction=interpreter.get_tensor(output_details[0]["index"])
print(prediction)
