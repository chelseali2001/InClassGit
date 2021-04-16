def divisors(a):
    for x in range(1, a + 1):
        if a % x == 0:
            print(x, " ", end='')

    print()

divisors(10)