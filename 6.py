# Возвести число x в степерь y. 2^10 = 1024

def power(x, y):
    if y == 0:
        return 1
    return x * power(x, y-1)


if __name__ == '__main__':
    print(power(2, 10))