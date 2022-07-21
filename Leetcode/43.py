def multiply(num1: str, num2: str):
    def karat(x,y):
        if len(str(x)) < 5 and len(str(y)) < 5:
            return x*y
        else:
            m = max(len(str(x)),len(str(y)))
            m2 = m // 2

            a = x // 10**(m2)
            b = x % 10**(m2)
            c = y // 10**(m2)
            d = y % 10**(m2)

            z0 = karat(b,d)
            z1 = karat((a+b),(c+d))
            z2 = karat(a,c)

            return (z2 * 10**(2*m2)) + ((z1 - z2 - z0) * 10**(m2)) + (z0)
    
    return str(karat(int(num1), int(num2)))

print(multiply(1341324167578234, 12347124252345341234))
    
    