import tensorflow as tf
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--weights", type=str, required=True, help="path of saved model/weights")

args = vars(ap.parse_args())

model = tf.keras.models.load_model(args["weights"])

model.summary()