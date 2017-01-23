#gotham filter code

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import data
%matplotlib inline

from skimage import data, filters, io
from skimage.io import imread

def get_image(url):
	image = imread(url) 
	original_image = skimage.img_as_float(image)
	return original_image


show = lambda x: io.imshow(x)

def split_image_into_channels(image):
	red_channel   = image[:,:,0]
	green_channel = image[:,:,1]
	blue_channel  = image[:,:,2]


def merge_channels(r,g,b):
	return np.stack([r,g,b],axis=2)



image = get_image("http://www.toursara.com/images/geo_pic.1363.10.jpg")
show(image)
r,g,b = split_image_into_channelsimage()

