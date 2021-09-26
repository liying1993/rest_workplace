def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # nums = len(height) - 1
    # max_area = 0
    # for i, i_val in enumerate(height):
    #     for j, j_val in enumerate(height):
    #         x_len = i - j
    #         y_len = i_val if i_val < j_val else j_val
    #         area = abs(x_len * y_len)
    #         if area > max_area:
    #             max_area = area
    # return max_area

    # 官方解法
    l_index, r_index = 0, len(height) - 1
    max_area = 0
    while l_index < r_index:
        area = min(height[l_index], height[r_index]) * (r_index - l_index)
        max_area = max(area, max_area)
        if height[l_index] <= height[r_index]:
            l_index += 1
        else:
            r_index -= 1
    return max_area




if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))