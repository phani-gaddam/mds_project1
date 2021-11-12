import numpy as np
from scipy.optimize import linprog
from scipy.fft import fft2


def optimize_s(C, y):
    # shape of C (y_dim,x_dim), shape of y (y_dim,)
    x_dim = C.shape[1]
    y_dim = y.shape[0]
    print(x_dim)
    print(y_dim)

    # defining an identity matrix of x_dim X x_dim for calculation
    # Identity = np.eye(x_dim)
    # # print(Identity)

    # # objective of the problem into the linear program
    # objective = np.concatenate([np.zeros(x_dim), np.ones(x_dim)])
    # # print(objective)
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

    # rhs_ineq = np.zeros(2 * x_dim)
    # # print(rhs_ineq)
    # #rhs_ineq_sparse = csr_matrix(rhs_ineq)

    # # defining equalities
    # lhs_eq = np.concatenate([C, np.zeros((y_dim, x_dim))], axis=1)
    # # print(lhs_eq)
    # lhs_eq_sparse = csr_matrix(lhs_eq)

    # rhs_eq = y
    # # print(rhs_eq)
    # #rhs_eq_sparse = csr_matrix(rhs_eq)

    # # defining bounds for each x and y x can be anything while y can only be greater than zero
    # bounds = [*((None, None) for _ in range(x_dim)), *((0, None)
    #                                                    for _ in range(x_dim))]
    # # print(bounds)
    # #bounds_sparse = csr_matrix(bounds)
    # # print(bounds_sparse)
    # result = linprog(c=objective, A_ub=lhs_ineq_sparse, b_ub=rhs_ineq,
    #                  A_eq=lhs_eq_sparse, b_eq=rhs_eq, bounds=bounds, method="highs-ds", options={'disp': True})


def finds():
    C = np.load("./Data_Green/C.npy")
    y = np.load("./Data_Green/y.npy")

    s = optimize_s(C, y)
    print(s)
    np.save("./Data_Green/computed_s.npy", s)
