def F(n):
    if n <= 5: return n
    if n % 5 == 0:
        return n + F(n//5 + 1)
    return n + F(n+6)


if __name__ == '__main__':
    for n in range(10000):
        try:
            print(F(12))
        except RecursionError:
            continue
