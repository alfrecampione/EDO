# N = numero total de la poblacion
# S = susceptibles => s = S/N
# I = infectados   => i = I/N
# R = removidos    => r = R/N


def improved_euler_method(f, g, j, x0: float, y0: float, z0: float, h):
    u1 = x0 + h * f(x0, y0, z0)
    v1 = y0 + h * g(x0, y0, z0)
    w1 = z0 + h * j(x0, y0, z0)

    x1 = x0 + (h / 2) * (f(x0, y0, z0) + f(u1, v1, w1))
    y1 = y0 + (h / 2) * (g(x0, y0, z0) + g(u1, v1, w1))
    z1 = z0 + (h / 2) * (j(x0, y0, z0) + j(u1, v1, w1))
    return x1, y1, z1


def runge_kutta_method(f, g, j, x0: float, y0: float, z0: float, h):
    F1 = lambda x: x(x0, y0, z0)
    F2 = lambda x: x(x0 + (h / 2) * F1(f), y0 + (h / 2) * F1(g), z0 + (h / 2) * F1(j))
    F3 = lambda x: x(x0 + (h / 2) * F2(f), y0 + (h / 2) * F2(g), z0 + (h / 2) * F2(j))
    F4 = lambda x: x(x0 + h * F3(f), y0 + h * F3(g), z0 + h * F3(j))
    x1 = x0 + (h / 6) * (F1(f) + 2 * F2(f) + 2 * F3(f) + F4(f))
    y1 = y0 + (h / 6) * (F1(g) + 2 * F2(g) + 2 * F3(g) + F4(g))
    z1 = z0 + (h / 6) * (F1(j) + F2(j) + F3(j) + F4(j))
    return x1, y1, z1


def get_results(s0, i0, t_max, h, f=improved_euler_method, alpha=0.26):
    ALPHA = alpha
    # s' = -s(t)i(t)
    s_der = lambda x, y, z: -x * y
    # i' = s(t)i(t) - ALPHA*i(t)
    i_der = lambda x, y, z: x * y - ALPHA * y
    # r' = ALPHA*i(t)
    r_der = lambda x, y, z: ALPHA * y

    n = round(t_max / h)
    r0 = 0
    if s0 <= 0 or i0 <= 0:
        raise Exception("Argument Exception")
    s = [s0]
    i = [i0]
    r = [r0]
    for j in range(n):
        s1, i1, r1 = f(s_der, i_der, r_der, s0, i0, r0, h)
        if s1 < 10 ** (-4):
            s1 = 0
        if i1 < 10 ** (-4):
            i1 = 0
        if r1 < 10 ** (-4):
            r1 = 0
        s.append(s1)
        i.append(i1)
        r.append(r1)
        s0, i0, r0 = s1, i1, r1
    return s, i, r
