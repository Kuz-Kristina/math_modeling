b = int(input('b = '))
q = int(input('q = '))
n = int(input('n = ')) 
B = b * q**(n - 1)
print()
while b <= B:
    print(b)
    b = b * q