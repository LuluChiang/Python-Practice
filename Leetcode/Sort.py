
from typing import ClassVar, List

class sortAlgorith:
    
    def BubbleSort(self, nums:List[int]) -> List[int]:
    # Worst: O(N^2)
    # Best: O(N^2)
        for base in range(len(nums) - 1):
            for bubble in range(len(nums) - 1 - base):
                if nums[bubble] > nums[bubble + 1]:
                    tmp = nums[bubble]
                    nums[bubble] = nums[bubble + 1]
                    nums[bubble + 1] = tmp
        return nums
    
class Solution:
# 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
#   Using binary search:
#
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        len_list = len(nums)
        head = 0
        tail = len_list - 1
        while head < tail - 1:
            idx = int((tail + head) / 2)
            if target == nums[idx]:
                return idx
            elif target > nums[idx]:
                head = idx
            elif target < nums[idx]:
                tail = idx 
        if target <= nums[head]:
            return head
        else:
            return tail