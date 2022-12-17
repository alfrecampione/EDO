# N = numero total de la poblacion
# S = susceptibles => s = S/N
# I = infectados   => i = I/N
# R = removidos    => r = R/N

ALPHA = 1


def get_results(s0, i0, h, n):
    r0 = 0
    if s0 <= 0 or i0 <= 0:
        raise Exception("Argument Exception")
    # s' = -s(t)i(t)
    s_der = lambda x, y: -x * y
    # i' = s(t)i(t) - ALPHA*i(t)
    i_der = lambda x, y: x * y - ALPHA * y
    # r' = ALPHA*i(t)
    r_der = lambda x: ALPHA * x
    s = [s0]
    i = [i0]
    r = [r0]
    for j in range(n):
        if s0 == 0 or i0 == 0:
            break
        s1 = s0 + h * s_der(s0, i0)
        i1 = i0 + h * i_der(s0, i0)
        r1 = r0 + h * r_der(i0)
        s.append(s1)
        i.append(i1)
        r.append(r1)
        s0 = s1
        i0 = i1
        r0 = r1
    return s, i, r
