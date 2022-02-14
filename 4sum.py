def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def three_sum(nums, target):
        result = []
        for j in range(len(nums)):
            start = j + 1
            end = len(nums) - 1
            while start < end:
                inner_sum = nums[start] + nums[end] + nums[j]
                if inner_sum == target:
                    result.append([nums[start], nums[end], nums[j]])
                    start += 1
                    end -= 1
                elif inner_sum > target:
                    end -= 1
                elif inner_sum < target:
                    start += 1
                if start == end:
                    break
        return result

    if len(nums) < 4:
        return []
    nums.sort()
    four_sum = []
    for i in range(len(nums)):
        new_target = target - nums[i]
        new_nums = nums[i+1:]
        if len(new_nums) < 3:
            continue
        answers = three_sum(new_nums, new_target)
        if answers:
            for ans in answers:
                ans.append(nums[i])
                ans.sort()
                if ans not in four_sum:
                    four_sum.append(ans)
    return four_sum

# 思路
# 把4sum，转成3sum去计算

if __name__ == '__main__':
    # nums = [1,0,-1,0,-2,2]
    nums = [-9,4,0,-3,6,3,-3,-9,-7,1,0,-7,-8,7,1]
    target = -9
    print(fourSum(nums, target))
