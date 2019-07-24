import tensorflow as tf
import numpy as np
import cv2

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="xray_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# to check input shape.
input_shape = input_details[0]['shape']
# to check output shape.
output_shape = output_details[0]['shape']

print("[INPUT SHAPE]: ", input_shape)
print("[OUTPUT SHAPE]: ", output_shape)

input_data = cv2.imread("normal.png")
input_data = cv2.resize(input_data, (224, 224))
input_data = np.expand_dims(input_data, axis=0)

input_data = input_data.astype(np.float32)

interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])

confidence = output_data[0][0]

print("+------------------------------+")

if confidence >= 0.5:
	print("PNEUMONIA ", confidence)
else:
	print("NORMAL ", confidence)