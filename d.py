
import numpy as np
import sklearn as d
a = int(input("yeah:"))
vocals = {"a":0, "b":22,"c":2}
if a == 2:
    x = np.array([vocals["a"],vocals["b"],vocals['b']])
    y = np.array([2,3,4])
    z = np.prod(x)
    print('f(x) + (y)', x + y)
    print('f(x)*f(y)',z)

    
