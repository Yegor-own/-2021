	
import cv2
import numpy as np
from PIL import Image


def predict(index)
	imgi = str(index)
	path1 = "images/"+imgi+".jpg"

	image = cv2.imread(path1)
	image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	ret, threshold_image = cv2.threshold(gray_image, 146, 255, cv2.THRESH_BINARY)

	path2 = "images/ice/"+imgi+".jpg"
	cv2.imwrite(path2, cv2.cvtColor(threshold_image, cv2.COLOR_BGR2RGB))

	im=np.array(Image.open(path2).convert('RGB'))

	white = [255, 255, 255]
	black = [0, 0, 0]

	w = np.count_nonzero(np.all(im==white,axis=2))
	b = np.count_nonzero(np.all(im==black,axis=2))
	return(w/b)


