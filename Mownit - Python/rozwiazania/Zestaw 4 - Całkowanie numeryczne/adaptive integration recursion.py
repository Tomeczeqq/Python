def f(x):
    return 1 / (1 + x**2)

def adaptive_integration(f, a, b):
    def adaptive_integration_recursion(f, a, b, fa, fb, fc, S):
        c = (a + b) / 2
        h = b - a
        d = (a + c) / 2
        e = (c + b) / 2
        fd = f(d)
        fe = f(e)
        Sleft = (fa + fd + fc) * h / 6
        Sright = (fc + fe + fb) * h / 6
        S2 = Sleft + Sright
        if abs(S2 - S) <= 1e-7:
            return S2 + (S2 - S) / 15
        else:
            return (adaptive_integration_recursion(f, a, c, fa, fc, fd, Sleft) +
                    adaptive_integration_recursion(f, c, b, fc, fb, fe, Sright))

    fa = f(a)
    fb = f(b)
    fc = f((a + b) / 2)
    S = (fa + 4 * fc + fb) * (b - a) / 6
    return adaptive_integration_recursion(f, a, b, fa, fb, fc, S)

print("Wynik metody całkowania adaptacyjnego:")
print(adaptive_integration(f, 0, 1))