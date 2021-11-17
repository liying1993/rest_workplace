def remove_dup(nums):
    p = 0
    q = 1
    while q < len(nums):
        if nums[p] != nums[q]:
            nums[p + 1] = nums[q]
            p += 1
        q += 1

    return p+1

if __name__ == '__main__':
    nums = [1,1,2]
    print(remove_dup(nums))