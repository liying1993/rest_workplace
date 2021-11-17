def remove_element(nums, val):
    left = 0
    right = len(nums)
    while left<right:
        if nums[left] == val:
            nums[left] = nums[right-1]
            right -= 1
        else:
            left += 1
    return left

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(remove_element(nums, val))
