import math as m
import astro_constants as ac
h = 100
A = m.pi / 3
B = m.pi / 6
v = (ac.g * h * (m.tan(B))**2/(2 * (m.cos(A))**2*(1 - m.tan(B) * m.tan(A))))**0.5
print('v =', v)


from astro_constants import k, e, h
from math import pi
T = 200
E = 300
N = 2 / pi**0.5 * h / (k * T)**(3/2) * e**(-E/(k*T)) * E**(T/2)
print('N =', N)