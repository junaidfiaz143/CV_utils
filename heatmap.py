from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model

from tensorflow.keras import preprocessing
from tensorflow.keras import backend as K
from tensorflow.keras import models
from tensorflow.keras.models import load_model

import tensorflow as tf
import numpy as np

import os
import cv2

image_size = 224

# load model
model = load_model("solar_model.h5")

os.system("cls")

input_name = "normal.png"

# load input image
input_image = cv2.imread(input_name)
# resize input image on which model is trained
input_image = cv2.resize(input_image, (224, 224))

temp_input_image = input_image

input_image = np.expand_dims(input_image, axis=0)
# ---------------------------------------------------

from tensorflow.keras.applications.inception_v3 import preprocess_input

x = preprocess_input(input_image)
print(x.shape)
print(input_image.shape)
# model.name="VGG"
preds = model.predict(input_image)[0]

# with tf.GradientTape() as tape:
# 	last_conv_layer = model.get_layer('conv2d_23')
# 	iterate = tf.keras.models.Model([model.inputs], [model.output, last_conv_layer.output])
# 	model_out, last_conv_layer = iterate(x)
# 	class_out = model_out[:, np.argmax(model_out[0])]
# 	grads = tape.gradient(class_out, last_conv_layer)
# 	print(grads)
# 	pooled_grads = np.mean(grads, axis=(0, 1, 2))

# heatmap = tf.reduce_mean(tf.multiply(pooled_grads, last_conv_layer), axis=-1)
# heatmap = np.maximum(heatmap, 0)
# heatmap /= np.max(heatmap)
# heatmap = heatmap.reshape((8, 8))

# heatmap = cv2.resize(heatmap, (temp_input_image.shape[1], temp_input_image.shape[0]))

# heatmap = cv2.applyColorMap(np.uint8(255*heatmap), cv2.COLORMAP_JET)

# temp_input_image = heatmap * 0.4 + temp_input_image

# cv2.imshow("PREDICTION", temp_input_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.resize(cv2.imread(orig), (res, res))
# cv2.resize(img, (res, res))