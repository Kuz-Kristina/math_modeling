def srednee_arifmeticheskoe(A):
    x = 0
    for i in A:
        n = len(A)
        a = i / n
        x = x + a
    return x
