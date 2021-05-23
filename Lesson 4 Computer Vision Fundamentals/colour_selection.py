import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#Read in the image and printout some stats
image=mpimg.imread('test.jpg')
print('This image is : ',type(image),'with dimensions',image.shape)

#Grab the x and y size and then make a copy of the image
ysize=image.shape[0]
xsize=image.shape[1]
'''
Always make a copy of arrays or other variables in Python. 
If instead, you say "a = b" 
then all changes you make to "a" will be reflected in "b" as well!
'''
color_select=np.copy(image)
#Define a color threshold in the 
#variables red_threshold, green_threshold,and blue_threshold 
#and populate rgb_threshold with these values.

red_threshold = 199
green_threshold = 200
blue_threshold = 199
rgb_threshold=[red_threshold, green_threshold, blue_threshold]

#Select any pixels below the threshold and set them to zero. 
'''
After that, all pixels that meet my color criterion (those above the threshold) will be retained,
and those that do not (below the threshold) will be blacked out.
'''

#Identify the pixels below the threshold
# Do a boolean or with the "|" character to identify
# pixels below the thresholds
thresholds=(image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])
color_select[thresholds]=[0,0,0]

# Display the image                 
plt.imshow(color_select)
plt.show()

mpimg.imsave("test-after-2.png", color_select)



