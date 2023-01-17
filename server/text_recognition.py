# credits to : https://tutorials-raspberrypi.de/raspberry-pi-texterkennung-ocr/

import cv2
import pytesseract
import numpy as np
import os
from pytesseract import Output


def text_recognition(media_t, port):

    img_path = os.path.join('media', f'output_{port}.{media_t}')
 
    img_source = cv2.imread(img_path)
    
    
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    
    def opening(image):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    
    
    def canny(image):
        return cv2.Canny(image, 100, 200)
    
    
    gray = get_grayscale(img_source)
    thresh = thresholding(gray)
    opening = opening(gray)
    canny = canny(gray)

    res = ""
    text = ""
    
    for img in [img_source, gray, thresh, opening, canny]:
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        n_boxes = len(d['text'])
    
        # back to RGB
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    
        for i in range(n_boxes):
            if int(d['conf'][i]) > 60:
                (text, x, y, w, h) = (d['text'][i], d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                # don't show empty text
                if text and text.strip() != "":
                    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    img = cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        
            if text not in res.split(" "):            
                res += (" " + text)

    return(res)
