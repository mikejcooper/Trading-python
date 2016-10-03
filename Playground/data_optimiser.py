from time import time

import numpy as np
import scipy.optimize as spo
import matplotlib.pyplot as plt

import trade as trade




def play():
    # Test data
    data = np.array([(1, 1), (2, 2), (3, 3), (4, 4)])
    # x and y vectors
    x = data[:, 0]
    y = data[:, 1]
    plt.plot(x,y,'x',label="Data points")

    # Using numpy
    z = np.polyfit(x, y, 2)
    f = np.poly1d(z)
    # calculate new x's and y's
    x_new = np.linspace(x[0], x[-1], 50)
    y_new = f(x_new)

    # plot numpy
    # plt.plot(x, y, 'o', x_new, y_new)
    # plt.xlim([x[0] - 1, x[-1] + 1])
    print f

    # Custom functions
    FIT = fit_poly(data,error_poly,2)
    print "Fitted line: c0 = {}, c1 = {}, c2 = {}".format(FIT[0],FIT[1], FIT[2])
    #           Y   =      Mx            +   C
    plt.plot(data[:,0], FIT[1]*data[:,0] + FIT[0], 'r--',linewidth=2.0,label = "Fitted line")
    plt.show()

def play1():
    object = trade.trade()
    print object.eyes
    print object.trade()


def error_poly(C, data):
    """Compute error between given polynomial model and observed data.

        :param C: numpy.poly1d object - representing polynomial co-efficients
        :param data: 2d array containing (x,y) points

        Returns error as a single real value
        """
    # sum of Y axis differences
    err = np.sum((data[:, 1] - (np.polyval(C,data[:,0]))) ** 2)
    return err

def fit_poly(data,error_func, degree):
    """Fit a polynomial to given data, using supplied error function

    :param data: 2d (x,y) array
    :param error_func: function that computes error between a polynomial and observed data
    Returns a polynomial that minimises the error fuction
    """
    # Initial guess for line model
    guess = np.poly1d(np.ones(degree + 1 , dtype=np.float32))

    # Optimiser
    min_result = spo.minimize(error_func, guess, args=(data,), method = 'SLSQP', options = {'disp': True})
    return np.poly1d(min_result.x)








if __name__ == "__main__":
    play1()