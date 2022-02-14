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


# 思路
# 也是双指针法，从左边开始移动指针，比较值，如果左边指针的值==val，可以把右边的指针指向的值换过来，然后右边的指针往左边挪动
if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(remove_element(nums, val))
