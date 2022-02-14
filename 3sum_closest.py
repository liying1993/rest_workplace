def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def two_sum(t_nums, target):
        l_index, r_index = 0, len(t_nums) - 1
        tmp_diff = None
        result = None
        while l_index < r_index:
            tmp_sum = t_nums[l_index] + t_nums[r_index]
            if tmp_sum == target:
                return target
            elif tmp_sum > target:
                r_index -= 1

            else:
                l_index += 1

            now_diff = abs(target - tmp_sum)
            if tmp_diff is None:
                tmp_diff = now_diff
                result = tmp_sum
            if tmp_diff is not None and now_diff < tmp_diff:
                tmp_diff = now_diff
                result = tmp_sum

            if l_index == r_index:
                break
        return result
    ans_diff = None
    three_sum = None
    nums.sort()
    for i in range(len(nums)):
        t_target = target - nums[i]
        t_nums = nums[i+1:]
        if len(t_nums) < 2:
            break
        res = two_sum(t_nums, t_target)
        if ans_diff is None:
            three_sum = nums[i] + res
            three_diff = abs(target - three_sum)
            ans_diff = three_diff
        else:
            three_sum = nums[i] + res
            three_diff = abs(target - three_sum)

        if ans_diff > three_diff:
            ans_diff = three_diff
            three_sum = nums[i] + res
    return three_sum

def func(nums, target):
    nums.sort()
    ans = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)):
        start = i+1
        end = len(nums) - 1
        while start < end:
            close_sum = nums[start] + nums[end] + nums[i]
            if abs(target - close_sum) < abs(target - ans):
                ans = close_sum
            if close_sum > target:
                end -= 1
            elif close_sum < target:
                start += 1
            else:
                return ans
    return ans

# 思路 和3sum一样的思路，也是使用双指针法，将第一个元素定点，后面的元素逐渐往中间靠拢

if __name__ == "__main__":
    nums = [-1,2,1,-4]
    # nums = [0,0,0,0]
    target = 1
    print(func(nums, target))