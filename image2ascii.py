import numpy as np
import cv2
import sys
# import matplotlib.pyplot as plt


def convert_grey(name):
    with open(name, 'rb') as f:
        image = cv2.imread(name)

    img_arr=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    r=img_arr[:,:,0]
    g=img_arr[:,:,1]
    b=img_arr[:,:,2]

    gama=1

    rw,gw,bw=0.2126,0.7152,0.0722

    gray_img=rw*r**gama+gw*g**gama+bw*b**gama
    # plt.imshow(gray_img, cmap='gray')  
    # plt.axis('off')                       #if you want to display
    # plt.show()                            #gray scale image
    return gray_img



def main():
    if len(sys.argv)<=1:
        print("No image path given")
        return 1

    name=sys.argv[1]
    arr="""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
    gray_img=convert_grey(name)
    file=open("save.txt","w")
    l=len(arr)-1
    for i in gray_img:
        for j in i:
            indx=round((j/255)*l)
            file.write(arr[indx])
        file.write("\n")
            

main()
