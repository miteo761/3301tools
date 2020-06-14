# As explained in; 'Formulas and Polynomials which Generate Primes and Fermat Pseudoprimes' p1, s13


def is_prime(n):
    if n & 1 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d = d + 2
    return 0


def emirp_generate(p, q, k):
    x = (p * q) + 10 ** k

    return x


def reverse(value):
    return int(str(value)[::-1])


def search_emirp(a, k):
    for k in range(1, k+1):
        print("k =", "{}:".format(k))

        for i in a:
            b = reverse(i)

            if is_prime(emirp_generate(i, b, k)) == 0:
                print(i, "-", emirp_generate(i, b, k))

            else:
                print(i, "-", "None")


emirp = [13, 17, 37, 79, 113]

search_emirp(emirp, 3)
