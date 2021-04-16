def divisors(a):
    for x in range(a):
        if a % x == 0:
            print(x, end='')

    print()

divisors(10)