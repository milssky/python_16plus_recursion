#Вычислить сумму элементов набора чисел

def sum_recursion(nums: list) -> int:
    if not nums:
        return 0

    summ = sum_recursion(nums[1:])
    return summ + nums[0]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    print(sum_recursion(nums))
    assert sum_recursion(nums) == 21
