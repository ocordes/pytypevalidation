"""

typevalidation/types.py

written by: Oliver Cordes 2019-07-04
changed by: Oliver Cordes 2019-07-19


"""

import numpy as np


basic_types = [bool, int, float, str, list, tuple]



def PosInt(x):
    try:
        x = int(x)
    except:
        raise TypeError('Can\'t convert value to integer')
    if x < 0:
        raise ValueError('Integer needs to be positive')

    return x


def PosFloat(x):
    try:
        x = float(x)
    except:
        raise TypeError('Can\'t convert value to float')
    if x < 0:
        raise ValueError('Float needs to be positive')



def Vector(x):
    if isinstance(x, (list, tuple)):
        if len(x) == 3:
            return np.array(x, dtype=np.float64)
        else:
            raise TypeError('List/tuple needs 3 entries for a vector')
    elif isinstance(x, np.ndarray):
        if x.shape == (3,):
            return x.copy()
        else:
            raise TypeError('numpy array needs 3 entries for a vector')
    elif isinstance(x, str):
        s = x.split(',')
        if len(s) == 3:
            return np.array([float(i) for i in s], dtype=np.float64)
        else:
            raise TypeError('string array needs 3 entries for a vector')
    else:
        raise TypeError('x is not of a suitable type for a vector')
