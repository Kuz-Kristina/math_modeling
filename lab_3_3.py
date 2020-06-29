from astro_constants import g
import numpy as np
v0x = float(input('v0x = '))
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
t = 0
n = 0
A = np.zeros((501, 3))
while t <= 5:
    x = x0 + v0x * t
    y = y0 + v0x * t - g * t**2 / 2
    A[n, 0] = t
    A[n, 1] = x
    A[n, 2] = y
    t = t + 0.01
    n = n + 1
print(A)