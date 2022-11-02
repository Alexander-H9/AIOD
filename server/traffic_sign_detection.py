# guide: https://github.com/ItsCosmas/Traffic-Sign-Classification

from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import cv2
import h5py
import pathlib

model_dir = pathlib.Path('/app/server/models/traffic_sign_classification.h5')
model = load_model(model_dir)

# Open Image for testing
img = cv2.imread("/app/server/media/sign1.png",1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def grayscale(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def equalize(img):
    img = cv2.equalizeHist(img)
    return img


def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    #normalize the images, i.e. convert the pixel values to fit btwn 0 and 1
    img = img/255
    return img

#Preprocess image
img = np.asarray(img)
img = cv2.resize(img, (32, 32))
img = preprocessing(img)

#plt.imshow(img, cmap = plt.get_cmap('gray'))
print(img.shape)

#Reshape reshape
img = img.reshape(1, 32, 32, 1)

#Test image
predict_x = model.predict(img)

classes_x=np.argmax(predict_x,axis=1)

print("The Predicted sign is in Class: "+ str(classes_x))