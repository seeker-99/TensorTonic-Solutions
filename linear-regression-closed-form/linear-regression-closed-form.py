import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X, y = np.asarray(X), np.asarray(y)
    x_transpose = np.transpose(X)
    prod_1 = x_transpose.dot(X)
    prod_2 = x_transpose.dot(y)
    inverse_x = np.linalg.inv(prod_1)
    ans = inverse_x.dot(prod_2)
    return ans