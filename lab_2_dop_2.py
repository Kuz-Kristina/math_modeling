a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
if a >= b + c or b >= a + c or c >= a + b:
    print('Данный треугольник не существует')
elif a == b == c:
    print('Данный треугольник является равносторонним')
elif a == b or b == c or a == c:
    print('Данный треугольник является равнобедренным')
else:
    print('Данный треугольник является разносторонним')