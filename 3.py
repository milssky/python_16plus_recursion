# Посчитать кол-во отрицательных чисел в списке

def count_negative_elements(nums: list) -> int:
    if not nums:
        return 0
    count = count_negative_elements(nums[1:])
    if nums[0] < 0:
        count += 1
    return count


if __name__ == '__main__':
    print(count_negative_elements([1, 2, -1, -666, -3, 4, 1]))
