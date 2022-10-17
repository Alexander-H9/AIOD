import os
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow import keras
import numpy as np
import pathlib


def init_obj_det():

    model_dir = pathlib.Path('models/ResNet50')
    
    if not model_dir.exists():
        model = ResNet50(weights='imagenet')
        model.compile()
        model.save(os.path.join('models', 'ResNet50'))
    else:
         model = keras.models.load_model(model_dir)
         model.compile()

    return model


def obj_det(model):

    img_path = os.path.join('media', 'output.jpg')

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)

    # print('Predicted:', decode_predictions(preds, top=3)[0])

    return(decode_predictions(preds, top=1)[0])


def get_picture_as_bytearray():
    img_path = os.path.join('media', 'b1.jpg')

    with open(img_path, "rb") as f:
        fileContent = f.read()

    byteArr = bytearray(fileContent)
    return byteArr
    


# get_picture_as_bytearray()

# run()