# As explained in; Formulas and Polynomials which Generate Primes and Fermat Pseudoprimes, page 102


def reverse(n):
    return int(str(n)[::-1])


def is_prime(n):
    if n & 1 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d = d + 2
    return 0


def quadratic_generate(n):
    x = 16*n**2 - 300*n + 1447

    return x


def search_quadratic(n):
    x = []

    for i in range(0, n):
        a = quadratic_generate(i)

        if is_prime(a) == 0:
            print(i, ":", a)
            x.append(a)

        else:
            print(i, "=", "None")

    return x


n = 30

print(search_quadratic(n))
