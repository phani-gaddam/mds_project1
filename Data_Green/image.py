import numpy as np
import imageio
from numpy.core.fromnumeric import amin
from Data_Green.q4 import findx


def greenImage():
    findx()
    x = np.load('./Data_Green/computed_x.npy')
    print(x.shape)
    x = x.reshape((100, 100), order='F')
    print(x.shape)
    oldRange = np.amax(x)-np.amin(x)
    newRange = 255
    x = (((x-np.amin(x))*newRange)/oldRange)+0
    # display(x)
    x = x.astype(np.uint8)
    imageio.imwrite("./Data_Green/generated_image.png", x)
