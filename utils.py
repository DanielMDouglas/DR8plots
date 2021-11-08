import numpy as np
from scipy.optimize import curve_fit

def quadr_sum(*args):
    return np.sqrt(sum(np.power(args, 2)))
