from tensorflow.keras.models import load_model
import tensorflow.keras as keras
import cv2
import numpy as np
import os

# load model
model = load_model("chest_xray_model.h5")

os.system("cls")

# input_name = "broken.jpg"
input_name = "test111.jpg"

# load input image
input_image = cv2.imread(input_name)
# resize input image on which model is trained
input_image = cv2.resize(input_image, (224, 224))

temp_input_image = input_image

input_image = np.expand_dims(input_image, axis=0)

print("Input Image Name:", input_name)
print("Input Image Dimension: ", input_image.shape)

# get predictions from model
predictions = model.predict(input_image)

print("CLASSES: {'NORMAL': 0, 'PNEUMONIA': 1}")
print("OUTPUT: ", predictions)

label = round(predictions[0][0])
temp_input_image = cv2.resize(temp_input_image, (422, 422))

if label == 0.0:
	cv2.putText(temp_input_image, "NORMAL", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
else:
	cv2.putText(temp_input_image, "PNEUMONIA", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

cv2.imshow("PREDICTION", temp_input_image)
# doc = keras.preprocessing.image.img_to_array(temp_input_image)

# import eli5
# print(eli5.show_prediction(model, doc))

# cv2.imshow("PREDICTION", eli5.show_prediction(model, doc))

cv2.waitKey(0)
cv2.destroyAllWindows()