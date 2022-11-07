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
img = cv2.imread("/app/server/media/sign3.png",1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

labels: dict = {
    0:"Speed limit (20 km/h)", 1: "Speed limit (30 km/h)", 2: "Speed limit (50 km/h)", 3: "Speed limit (60 km/h)", 4: "Speed limit (70 km/h)", 5: "Speed limit (80 km/h)", 
    6: "End of speed limit (80 km/h)", 7: "Speed limit (100 km/h)", 8: "Speed limit (120 km/h)", 9: "No passing", 10: "No passing for vehicles over 3.5 metric tons",
    11: "Right-of-way at the next intersection", 12: "Priority road", 13: "Yield", 14: "Stop", 15: "No vehicles",
    16: "Vehicles over 3.5 metric tons prohibited", 17: "No entry", 18: "General caution", 19: "Dangerous curve to left", 20: "Dangerous curve to right",
    21: "Double curve", 22: "Bumpy road", 23: "Slippery road", 24: "Road narrows on the right", 25: "Road work", 
    26: "Traffic signals", 27: "Pedestrians", 28: "Children crossing", 29: "Bicycles crossing", 30: "Beware of ice/snow",
    31: "Wild animals crossing", 32: "End of all speed passing limits", 33: "Turn right ahead", 34: "Turn left ahead", 35: "Ahead only",
    36: "Go straight or right", 37: "Go straight or left", 38: "Keep right", 39: "Keep left", 40: "Roundabout mandatory",
    41: "End of no passing", 42: "End of no passing by vehicles over 3.5 metric tons"
}


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

print(f'The predicted class {classes_x} is a: {labels[int(classes_x)]}')