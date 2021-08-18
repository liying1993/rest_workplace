def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 我的解法
    # for i, num in enumerate(nums):
    #     other_num = target - num
    #     nums[i] = "nan"
    #     if other_num in nums:
    #         other_index = nums.index(other_num)
    #         return [i, other_index]
    # 官方解法
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)
