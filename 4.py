# Сумма чисел в списке, но с поддержкой вложенных списков
# [1,2,3, [4,5,6]] -> 21


def calc_sum_extended(nums: list) -> int:
    summ = 0

    for element in nums:
        if not isinstance(element, list):
            summ += element
        else:
            summ += calc_sum_extended(element)
    return summ


def sum_recursion(nums: list) -> int:
    if not nums:
        return 0
    if isinstance(nums[0], list):
        return sum_recursion(nums[0])
    summ = sum_recursion(nums[1:])
    return summ + nums[0]


if __name__ == '__main__':
    print(calc_sum_extended([1, 2, 3, [4, 5, 6, [7, [8, [9, 10]]]]]))
    print(sum_recursion([1, 2, 3, [4, 5, 6, [7, [8, [9, 10]]]]]))
