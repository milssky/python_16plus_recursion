# Перевод из десятичной в двоичную СС. 17 -> 10001. Не использовать строки


def dec2bit(n: int, power=0) -> int:
    if n == 0:
        return 0
    return dec2bit(n // 2, power + 1) + n % 2 * 10 ** power


if __name__ == '__main__':
    assert dec2bit(17) == 10001
    print(dec2bit(19))
