import numpy as np
from q5_content.q3 import finds


def findx(path):
    finds(path)
    print("solving for x")
    A_inv = np.load(path+"A_inv.npy")
    s = np.load(path+"computed_s.npy")
    # since x=As
    A = np.linalg.inv(A_inv.astype(np.float64))
    x = A.dot(s)
    np.save(path+"computed_x.npy", x)
