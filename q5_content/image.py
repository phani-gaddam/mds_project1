import numpy as np
import imageio
from numpy.core.fromnumeric import amin
from q5_content.q4 import findx


def image(path):
    findx(path)
    print("Making a image")
    x = np.load(path+"computed_x.npy")
    x = x.reshape((100, 100), order='F')
    oldRange = np.amax(x)-np.amin(x)
    newRange = 255
    x = (((x-np.amin(x))*newRange)/oldRange)+0
    # display(x)
    x = x.astype(np.uint8)
    imageio.imwrite(path+"generated_image.png", x)
    print("Image generaeted in {}", path)
