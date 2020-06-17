print('')
print('ax^2 + bx + c = 0')
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
print('')
D = b**2 - 4 * a * c
if D < 0:
    print('Нет корней')
elif D == 0:
    x = - b / (2 * a)
    print('x=', x)
else:
    x = (-b + D**0.5) / (2 * a)
    print('x1 =', x)
    x = (-b - D**0.5) / (2 * a)
    print('x2 =', x)