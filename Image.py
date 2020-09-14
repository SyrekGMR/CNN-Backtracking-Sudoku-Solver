import cv2
import numpy as np
import operator


# Load image and convert into grayscale
def load_image(file):
    img = cv2.imread("Sudoku_Grids/Grid1.png", cv2.IMREAD_GRAYSCALE)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    return img

# Image modifications to highlight contours

def img_mod(img):
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    img = cv2.bitwise_not(img, img) 
    kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]],np.uint8)
    img = cv2.dilate(img, kernel)

    return img

# Use CV2 to detect contours, identifying Sudoku grid within the image

def locate(img):
    # Locates contours within image, returns cropped image around contours
    contours, h = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    polygon = contours[0]

    bottom_right, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in
                        polygon]), key=operator.itemgetter(1))
    top_left, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in
                    polygon]), key=operator.itemgetter(1))
    bottom_left, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in
                        polygon]), key=operator.itemgetter(1))
    top_right, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in
                    polygon]), key=operator.itemgetter(1))

    pp = np.array([polygon[top_left][0], polygon[top_right][0], polygon[bottom_right][0], polygon[bottom_left][0]])

    img_n = img[min(pp[:, 1]):max(pp[:, 1]), min(pp[:, 0]):max(pp[:, 0]),]

    return img_n