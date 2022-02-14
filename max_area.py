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

# 思路：
# 使用双指针法，最左和最右的指针向中间靠近。
# 面积的计算是一个长方形的长✖️宽，长是两底之差，宽是较短的那根柱子
# 指针移动的规则是哪跟短，就选哪根移动。为什么这样呢？因为移动短板，下一个面积可能增大或者减小，但是一定长板，下一个面积一定减小


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))