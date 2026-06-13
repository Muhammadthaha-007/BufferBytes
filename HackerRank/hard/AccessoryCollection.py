
def acessoryCollection(L, A, N, D):

    if D > A or N < D or N > L:
        return "SAD"

    if D == 1:
        return str(L * A)

    best = 0

    a2_max = (N - 1) // (D - 1)

    for a2 in range(a2_max, 0, -1):

        a1 = N + (a2 - 1) - a2 * (D - 1)

        n = (L - a1) // a2
        a3 = (L - a1) % a2

        if n > A - 1 or (n == A - 1 and a3 > 0):
            break

        total = (
            A * a1
            + (A - 1 + A - n) * n // 2 * a2
            + a3 * (A - n - 1)
        )

        if total <= best:
            break

        best = total

    return str(best) if best else "SAD"

print(acessoryCollection(6, 5, 3, 2))