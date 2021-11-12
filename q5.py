import numpy as np
import imageio
from numpy.core.fromnumeric import amin
from sklearn.preprocessing import normalize
from q5_content.image import image

dict = {0: "./Data_Red/", 1: "./Data_Green/", 2: "./Data_Blue/"}


final = np.zeros((100, 100, 3))


for i in range(0, 3):
    image(dict[i])
    x = np.load(dict[i]+'computed_x.npy')
    x = (np.reshape(x, (100, 100)))
    final[:, :, i] = x.T


oldRange = (np.amax(final)-np.amin(final))
newRange = (255-0)
final = (((final-np.amin(final))*newRange)/oldRange)+0

final = (final.astype(np.uint8))

imageio.imwrite("generated_image_q5.png", final)
