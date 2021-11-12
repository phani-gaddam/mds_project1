import numpy as np
from Data_Green.q3 import finds


def findx():
    finds()
    A_inv = np.load("./Data_Green/A_inv.npy")
    s = np.load("./Data_Green/computed_s.npy")
    print(s)
    # since x=As
    A = np.linalg.inv(A_inv.astype(np.float64))
    x = A.dot(s)
    print(x)
    np.save("./Data_Green/computed_x.npy", x)
