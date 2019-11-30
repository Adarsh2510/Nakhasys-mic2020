from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
from io import BytesIO
import re, time, base64
from PIL import Image

def Centroid():
    im = Image.open("./uploads/image.png")
    immat = im.load()
    (X, Y) = im.size
    m = np.zeros((X, Y))

    for x in range(X):
        for y in range(Y):
            m[x, y] = immat[(x, y)] != (255, 255, 255)
    m = m / np.sum(np.sum(m))
    dx = np.sum(m, 1)
    dy = np.sum(m, 0)

# expected values
    cx = np.sum(dx * np.arange(X))
    cy = np.sum(dy * np.arange(Y))
    

    im1 = im.crop((cx-100, cy-30, cx+70, cy+100))
    im1.save("./images/img.png")
    return im1

def Check(hex_colors):
  if "#36454f" in hex_colors:
    return True
  if "#282C35" in hex_colors :
    return True
  if "#0f0f0f" in hex_colors:
    return True
  if "#343434" in hex_colors:
    return True
  if "#4e4b4a" in hex_colors:
    return True
  if "#3b3c36" in hex_colors:
    return True
  if "#565350" in hex_colors:
    return True
  if "#464647" in hex_colors:
    return True
  if "#906967" in hex_colors or "#676990" in  hex_colors:
    return True
  else:
    return False
    
def  RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
def HEX2RGB(color):
    
    print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))


def CancerCheck(image_path):
    image=cv2.imread(image_path)
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    clf = KMeans(n_clusters = 10)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)

    center_colors = clf.cluster_centers_
# We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
   
    

    result=Check(hex_colors)
    if result==True:
      return True


def ChecKDisease():
    
    
    #Centroid()

    cap=cv2.imread("./images/img.png")
    hsv_frame=cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)
    ##yellow color
    low_yellow=np.array([20,100,100])
    high_yellow=np.array([30,255,255])
    yellow_mask=cv2.inRange(hsv_frame,low_yellow,high_yellow)
    yellow=cv2.bitwise_and(cap,cap,mask=yellow_mask)
    #cv2.imshow("yellow",yellow)

    ##Red Color Ranges
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    Red_mask=cv2.inRange(hsv_frame,lower_red,upper_red)
    Red=cv2.bitwise_and(cap,cap,mask=Red_mask)
    #cv2.imshow("Red",Red)

    #Green Color Ranges
    lower_green=np.array([36, 25, 25])
    upper_green=np.array([70, 255,255])
    #green_mask=cv2.inRange(hsv_frame,lower_green,upper_green)
    #green=cv2.bitwise_and(cap,cap,mask=green_mask)
    #cv2.imshow("Green",green)

    #purple
    lower_purple=np.array([140, 100, 100])
    upper_purple=np.array([160, 255, 255])
    purple_mask=cv2.inRange(hsv_frame,lower_purple,upper_purple)
    purple=cv2.bitwise_and(cap,cap,mask=purple_mask)
    #cv2.imshow("Purple",purple)



    #blue color
    lower_blue = np.array([94,80,2])
    upper_blue = np.array([126,255,255])
    blue_mask=cv2.inRange(hsv_frame,lower_blue,upper_blue)
    blue=cv2.bitwise_and(cap,cap,mask=blue_mask)
    #cv2.imshow("blue",blue)


    #pink color range
    low_pink=np.array([147,100,100])
    high_pink=np.array([187, 255, 255])
    pink_mask=cv2.inRange(hsv_frame,low_pink,high_pink)
    pink=cv2.bitwise_and(cap,cap,mask=pink_mask)
    #cv2.imshow("pink",pink)

    ##gray color
    low_gray=np.array([15, 10, 50])
    high_gray=np.array([179, 50, 255])
    gray_mask=cv2.inRange(hsv_frame,low_gray,high_gray)
    gray=cv2.bitwise_and(cap,cap,mask=gray_mask)
    #cv2.imshow("grey",gray)
    #black color
    lower_black = np.array([0,0,0])
    upper_black = np.array([50,50,100])
    black_mask=cv2.inRange(hsv_frame,lower_black,upper_black)
    black=cv2.bitwise_and(cap,cap,mask=black_mask)
    #cv2.imshow("black",black)

    lower_white = np.array([0,0,168])
    upper_white = np.array([172,111,255])
    white_mask=cv2.inRange(hsv_frame,lower_white,upper_white)
    white=cv2.bitwise_and(cap,cap,mask=white_mask)
   # cv2.imshow("white",white)
    
    





    ratio_yellow=cv2.countNonZero(yellow_mask)/(cap.size/3)
    yellow_percentage=np.round(ratio_yellow*100,2)
    #print('yellow color percentage',yellow_percentage)
    ratio_blue=cv2.countNonZero(blue_mask)/(cap.size/3)
    blue_percentage=np.round(ratio_blue*100,2)
    #print('blue color percentage',blue_percentage)
    ratio_gray=cv2.countNonZero(gray_mask)/(cap.size/3)
    gray_percentage=np.round(ratio_gray*100,2)
    #print("gray color percentage",gray_percentage)
    ratio_purple=cv2.countNonZero(purple_mask)/(cap.size/3)
    purple_percentage=np.round(ratio_purple*100,2)
    #print("purple color percemtage",purple_percentage)
    ratio_red=cv2.countNonZero(Red_mask)/(cap.size/3)
    red_percentage=np.round(ratio_red*100,2)
    #print("red percentage",red_percentage)
    ratio_white=cv2.countNonZero(white_mask)/(cap.size/3)
    white_percentage=np.round(ratio_white*100,2)
    #print("white_percentage",white_percentage)
    result=""

    if yellow_percentage > blue_percentage and  yellow_percentage > gray_percentage and yellow_percentage > purple_percentage and yellow_percentage > white_percentage and yellow_percentage > red_percentage:
        result="yellow"
        print(result)
    elif blue_percentage> yellow_percentage and blue_percentage> gray_percentage and blue_percentage> purple_percentage and blue_percentage>white_percentage and blue_percentage > red_percentage:
        result="blue"
        print(blue)
    elif purple_percentage>yellow_percentage and purple_percentage>blue_percentage and purple_percentage>gray_percentage and purple_percentage>white_percentage and purple_percentage > red_percentage:
        result="purple"
        print(purple)
    elif red_percentage>yellow_percentage and red_percentage>blue_percentage and red_percentage>purple_percentage and red_percentage>white_percentage and red_percentage>gray_perecentage :
        result="red"
        print(result)
    elif white_percentage>red_percentage and white_percentage>yellow_percentage and white_percentage>purple_percentage and white_percentage>blue_percentage and white_percentage>gray_percentage:
        result="white"
        print(result)
    else:
        result="pink"
        print(result)
        


#codec=""   # variable for decoding base64 data
#getI420FromBase64(codec)  ##function for decoding the base64 data
Centroid()  #fuction to  find the nail/center of the image 

        
if CancerCheck("./images/img.png") is True:  ## calling function to check the Cancer
    print("person is Suffering from Cancer")                                 ## if this true another function call for checkDisease doesnot run
    
    
else:
    ChecKDisease()
   

cv2.waitKey()
cv2.destroyAllWindows()
