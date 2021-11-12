import numpy as np

if __name__ == "__main__":
    A_inv = np.load("./A_inv.npy")
    s = np.load("./computed_s.npy")
    print(s)
    # since x=As
    A = np.linalg.inv(A_inv.astype(np.float64))
    x = A.dot(s)
    print(x)
    np.save("./computed_x.npy", x)
