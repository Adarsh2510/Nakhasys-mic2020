
import cv2 
import numpy as np

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
    

    im1 = im.crop((cx-15, cy-15, cx+15, cy+15))
    im1.save("./images/img.png")
    return im1
    

Centroid()
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
low_gray=np.array([0, 5, 50])
high_gray=np.array([179, 50, 255])
gray_mask=cv2.inRange(hsv_frame,low_gray,high_gray)
gray=cv2.bitwise_and(cap,cap,mask=gray_mask)
#cv2.imshow("grey",gray)



ratio_yellow=cv2.countNonZero(yellow_mask)/(cap.size/3)
yellow_percentage=np.round(ratio_yellow*100,2)
#print('yellow color percentage',yellow_percentage)
ratio_blue=cv2.countNonZero(blue_mask)/(cap.size/3)
blue_percentage=np.round(ratio_blue*100,2)
#print('blue color percentage',blue_percentage)
ratio_gray=cv2.countNonZero(gray_mask)/(cap.size/3)
gray_percentage=np.round(ratio_gray*100,2)
#print('gray color percentage',gray_percentage)
ratio_purple=cv2.countNonZero(purple_mask)/(cap.size/3)
purple_percentage=np.round(ratio_purple*100,2)
#print("purple color percemtage",purple_percentage)

if yellow_percentage>float(0):
    result="yellow"
elif blue_percentage>float(0):
    result="blue"
elif purple_percentage>float(0):
    result="purple"
else:
    result="pink"
    

print(result)

cv2.waitKey()
cv2.destroyAllWindows()
