def polynomial_factory(coeff):
    def poly(x):
        p = 0
        for c in coeff:
            p = p * x + c
        return p
    return poly

p1 = polynomial_factory([4, -7, 2, 5])

for i in range(10):
    print(p1(i))