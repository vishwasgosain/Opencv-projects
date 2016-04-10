import cv2

image = cv2.imread('k.jpg')
print("Which format do you want to convert the image to?")
a= raw_input()
if (a== "jpg"):
	cv2.imwrite('no.jpg',image)

elif (a== "png"):
	cv2.imwrite('no.png',image)

elif (a== "bmp"):
	cv2.imwrite('no.bmp',image)

else:
	print("Can't convert the given function into the format specified by you")

print ("Done bro")
