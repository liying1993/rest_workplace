def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # 第一遍
    # ans = []
    # nums.sort()
    #
    # def two_sum(t_nums, target):
    #     s_nums = set()
    #     for val in t_nums:
    #         o_val = target - val
    #         if o_val in s_nums:
    #             return [val, o_val]
    #         s_nums.add(val)
    #     return
    #
    # for i, i_val in enumerate(nums):
    #     t_nums = nums[i + 1:]
    #     two_target = 0 - i_val
    #     two_result = two_sum(t_nums, two_target)
    #     if two_result is not None:
    #         two_result.append(i_val)
    #         ans.append(two_result)
    # return ans

    # 第二遍
    def two_sum(t_nums, target):
        result = []
        l_index, r_index = 0, len(t_nums) - 1
        while l_index < r_index:
            tmp_sum = t_nums[l_index] + t_nums[r_index]
            if tmp_sum == target:
                while l_index < r_index and t_nums[l_index] == t_nums[l_index+1]:
                    l_index += 1
                # l_index += 1
                while l_index < r_index and t_nums[r_index] == t_nums[r_index-1]:
                    r_index -= 1
                result.append([-target, t_nums[l_index], t_nums[r_index]])
                l_index += 1

                r_index -= 1
            elif tmp_sum > target:
                r_index -= 1
            else:
                l_index += 1

            if l_index == r_index:
                break
        return result
    ans = []
    nums.sort()
    pre_value = None
    for i in range(len(nums)):
        cur_value = nums[i]
        if cur_value == pre_value:
            continue
        else:
            pre_value = cur_value
        target = -cur_value
        t_nums = nums[i+1:]
        if len(t_nums) < 2:
            break
        res = two_sum(t_nums, target)
        if res:
            ans.extend(res)
    return ans


    # 官方
    # n = len(nums)
    # nums.sort()
    # ans = list()
    #
    # for first in range(n):
    #     if first > 0 and nums[first] == nums[first - 1]:
    #         continue
    #     third = n - 1
    #     target = -nums[first]
    #
    #     for second in range(first + 1, n):
    #         if second > first + 1 and nums[second] == nums[second - 1]:
    #             continue
    #         while second < third and nums[second] + nums[third] > target:
    #             third -= 1
    #         if second == third:
    #             break
    #         if nums[second] + nums[third] ==target:
    #             ans.append([nums[first], nums[second], nums[third]])
    # return ans


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    # nums = [0,0,0,0]
    print(threeSum(nums))