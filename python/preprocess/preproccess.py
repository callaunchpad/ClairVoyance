import numpy as np
import os



def crop(arr, x_left, x_right, y_top, y_bottom):
    """
    Assume arr is a numpy array of the image with 4 dimensions:
    [num_images, channels, rows, columns]
    Need to crop this array in the last two dimensions according to params.
    """
    return arr[:,:,y_top:y_bottom,x_left:x_right]
