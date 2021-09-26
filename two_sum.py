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


def remove_elements(head: ListNode, val):
    dummy_head = ListNode(next=head)
    cur = dummy_head
    while(cur.next != None):
        if(cur.next.val == val):
            cur.next = cur.next.next
        else:
            cur = cur.next
        return dummy_head.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self._head = Node(0)
        self._count = 0

    def get(self, index):
        if 0 <= index < self._count:
            node = self._head
            for _ in range(index+1):
                node = node.next
            return node.val
        else:
            return -1

    def  add_at_head(self, val):
        self.add_at_index(0, val)

    def add_at_tail(self, val):
        self.add_at_index(self._count, val)

    def add_at_index(self, index, val):
        if index < 0:
            index = 0
        elif index > self._count:
            return

        self._count += 1

        add_node = Node(val)
        prev_node, current_node = None, self._head
        for _ in range(index + 1):
            prev_node, current_node = current_node, current_node.next
        else:
            prev_node.next, add_node.next = add_node, current_node

    def delete_at_index(self, index):
        if 0 <= index < self._count:
            self._count -= 1
            prev_node = current_node = None, self._head
            for _ in range(index+1):
                prev_node, current_node = current_node, current_node.next
            else:
                prev_node.next, current_node.next = current_node.next, None



if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = twoSum(nums, target)
    print(result)
