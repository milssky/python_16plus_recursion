# Разворот числа. 123 -> 321. Не используя строк

def reverse_number(n: int) -> int:
    if n == 0:
        return 0
    temp_n = n
    power = -1
    while temp_n > 0:
        power += 1
        temp_n //= 10
    last_digit = n % 10
    result = last_digit * 10**power
    return result + reverse_number(n//10)


def reverse_number_2(n: int, reversed_num=0) -> int:
    if n == 0:
        return reversed_num
    last_digit = n % 10
    return reverse_number_2(n // 10, reversed_num * 10 + last_digit)


if __name__ == '__main__':
    print(reverse_number_2(123))
