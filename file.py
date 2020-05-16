import cv2
import numpy as np 
import math
import cmath
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def exponential(c,b,f):
	value = int(c*(b**f-1))
	if(value>255):
		return 255
	if(value<0):
		return 0
	return value


def raise_to(c,r,f):
	value = int(c*(f**r))
	if(value>255):
		return 255
	if(value<0):
		return 0
	return value

def logarithm(c,f):
	value = int(c*math.log(1+f,10))
	if(value>255):
		return 255
	if(value<0):
		return 0
	return value
	
def main(cons,cons1,img):
	height, width = img.shape

	for y in range(0,width):
		for x in range(0,height):
			img[x,y] = exponential(cons,cons1,img[x,y])
			#img[x,y] = raise_to(cons,cons1,img[x,y])
	strr = str(cons)+"_"+str(cons1)+".jpg"
	cv2.imwrite(strr,img);


Tk().withdraw()
filename = askopenfilename()

#values = [0.5,0.1,0.05,0.01,0.005,0.001]#[40,60,80]
#constan = [1,1.5,2]
values = [1,5,10,15,20,25,40,50]#[40,60,80]
constan = [1.01,1.005]

for i in values:
	for j in constan:
		imgen = cv2.imread(filename)
		img = cv2.cvtColor(imgen, cv2.COLOR_BGR2GRAY)
		main(i,j,img)




