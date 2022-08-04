def mirrorReflection(p: int, q: int):
    """add virtual image: meet corner <==> m * q == n * p """
    for n in range(1, 1001):
        if p*n %q == 0:
            m = p*n // q
            if n%2 ==  0:
                if m %2 == 1:
                    return 0
            else:
                if m % 2 == 0:
                    return 2
                else:
                    return 1
                
                
print(mirrorReflection(5, 4))
    
    