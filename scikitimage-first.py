import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import data , io, filters
from skimage.io import imread 

#%matplotlib inline

show = lambda x: io.imshow(x)

#loading sample images from skimage data module
image = data.camera() # or any NumPy array!
io.imshow(image)

#scikit loading images from URL
url = "http://www.toursara.com/images/geo_pic.1363.10.jpg"
image = imread(url) 
io.imshow(image)

#blurred image
blurred = filters.gaussian(image, sigma=10, multichannel=True)
#io.imshow(blurred)
show(blurred)


#sharpen image
def sharpen(image , a,b , sigma=10):
	blurred = filters.gaussian(image,sigma=sigma, multichannel=True)
	sharper = np.clip(image * a - blurred * b , 0, 1.0)
	return sharper

sharper = sharpen(original_image, 1.3, 0.3)
show(sharper)




