import pandas as pd
import argparse
import cv2

## Using argument parser to directly give the image path from the command prompt ##
argprs = argparse.ArgumentParser()
argprs.add_argument('-i','--image',required=True, help="Image Path")
arguments = vars(argprs.parse_args())
image_path = arguments['image']

#Reading the image with opencv
img = cv2.imread(image_path)

# Global declaration
clicked = False
r = g = b = xpos = ypos = 0

## Reading the CSV colors file ##
#giving names to each attribute
index_naming = ['Color','Color_Name','hex','R','G','B']
csv = pd.read_csv("datasets/colors_dataset.csv", names=index_naming, header=None) #We didnt have names in csv file so header=none

## Calculating the distance to get Color Name ##
#Will reflect back to the nearest distant color from the list #
def getColorName(R,G,B):
    minimum = 10000
    for i in range (len(csv)):
        d = abs(R - int(csv.loc[i,"R"])) + abs(G - int(csv.loc[i,"G"])) + abs(B - int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i, 'Color_Name']
    return cname

## Draw_funct_col ##
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x # x coordinate location
        ypos = y # y coordinate location
        b,g,r = img[y,x]
        b = int(b) #Blue value converted to integer
        g = int(g) #Green value converted to integer
        r = int(r) #Red value converted to integer

## Setting p mouse click and callback for interactive demonstration ##
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while(1):
    cv2.imshow("image",img)
    if(clicked):
        #cv2.rectangle -> -1 will fill the rectangle completely
        cv2.rectangle(img, (20,20), (750,50), (b,g,r), -1)

        #Creating text string to display the color name and the rgb value
        color_named_text = getColorName(r,g,b) + ' R='+str(r) + ' G='+str(g)+' B='+str(b)

        #cv2.putText
        cv2.putText(img, color_named_text, (40,40), 2, 0.8, (255,255,255), 2, cv2.LINE_AA)

        #For extremely light colors display black
        if(r+g+b>=600):
            cv2.putText(img,color_named_text,(40,40), 2, 0.8, (0,0,0), 2, cv2.LINE_AA)
        clicked = False

        #Break the loop when 'esc' is detected
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()