# Максимальный элемент списка. [1,2,3] -> 3

def max_element_in_list(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    max_element = max_element_in_list(nums[1:])
    if max_element > nums[0]:
        return max_element
    return nums[0]


if __name__ == '__main__':
    print(max_element_in_list([1,2,3]))