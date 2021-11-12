import numpy as np
from scipy.optimize import linprog
from scipy.fft import fft2


def optimize_s(C, y):
    # shape of C (y_dim,x_dim), shape of y (y_dim,)
    x_dim = C.shape[1]
    y_dim = y.shape[0]
    print(x_dim)
    print(y_dim)

    obj = np.ones(2*x_dim)
    print(obj.shape)

    lhs_eq = np.concatenate((C, -1*C), axis=1)
    rhs_eq = y

    bound_upper = np.full([2*x_dim, 1], np.inf)
    bound_lower = np.full([2*x_dim, 1], 0)
    bounds = np.concatenate((bound_lower, bound_upper), axis=1)

    result = linprog(obj, A_eq=lhs_eq, b_eq=rhs_eq,
                     bounds=bounds, options={'disp': True})
    value = result.x
    s = value[0:x_dim]-value[x_dim:]
    return np.array(s)


if __name__ == "__main__":
    C = np.load("./C.npy")
    y = np.load("./y.npy")

    s = optimize_s(C, y)
    print(s)
    np.save("./computed_s.npy", s)
