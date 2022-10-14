import tensorflow as tf
import pathlib
# import tqdm     # for progress bar
import os
import numpy as np
from tensorflow.keras.preprocessing import image

# https://www.codeproject.com/script/Content/ViewReadingList.aspx?rlid=39

tflite_model_file = pathlib.Path('models/ssd_mobilenet_v1_coco_tflite/ssd_mobilenet_v1_1_metadata_1.tflite')

with open(tflite_model_file, 'rb') as fid:
    tflite_model = fid.read()

interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

print(input_index)
print(output_index)

img_path = os.path.join('media', 'b1.jpg')

img = image.load_img(img_path, target_size=(300, 300))
x = np.expand_dims(img, axis=0)

# Gather results for the randomly sampled test images
predictions = []

test_labels, test_imgs = [], []

interpreter.set_tensor(input_index, x)
interpreter.invoke()
predictions.append(interpreter.get_tensor(output_index))

print(predictions)