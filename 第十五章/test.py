
import numpy as np
a = [1, -0.6, 0.7]
b = [0.04, 0.08, 0.4]
poles = np.roots(a)
zeros = np.roots(b)
print('极点:', poles)
print('极点模值:', np.abs(poles))
print('零点:', zeros)
print('零点模值:', np.abs(zeros))

