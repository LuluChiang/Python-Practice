
from typing import ClassVar, List

class sortAlgorith:
    def BubbleSort(self, nums:List[int]) -> List[int]:
    # Worst: O(N^2)
    # Best: O(N)!!
        for base in range(len(nums) - 1):
            no_swap = True
            for bubble in range(len(nums) - 1 - base):
                if nums[bubble] > nums[bubble + 1]:
                    # nums[bubble], nums[bubble + 1] = nums[bubble + 1], nums[bubble]
                    tmp = nums[bubble]
                    nums[bubble] = nums[bubble + 1]
                    nums[bubble + 1] = tmp
                    no_swap = False
            if no_swap:
                break
        return nums
    
    def InsertionSort(self, nums:List[int]) -> List[int]:
        # Worst: O(N^2)
        # Best: O(N)
        for idx in range(len(nums) - 1):
            target = nums[idx + 1]
            for idx2 in range(idx, -1, -1):
                if target > nums[idx2]:
                    nums[idx2 + 1] = target
                    break
                else:
                    nums[idx2 + 1] = nums[idx2]
                    if idx2 == 0:
                        nums[0] = target            
        return nums

    def SelectionSort(self, nums:List[int]) -> List[int]:
    # O(N^2)
        for idx in range(len(nums)):
            minnum = nums[idx]
            minidx = idx
            for idx2 in range(idx + 1, len(nums)):
                if nums[idx2] < minnum:  
                    minnum = nums[idx2]
                    minidx = idx2
            nums[idx], nums[minidx] = nums[minidx], nums[idx]
        return nums
    
    def QuickSort(self, nums:List[int]) -> List[int]:
        # Worst O(N^2)
        # Best = Avg = O(NlogN)
        if len(nums) <= 1:
            return nums
        pivot = nums[-1]
        small = -1  # 0 ~ small <= pivot
        large = 0   # small + 1 ~ large > pivot
        for idx in range(len(nums) - 1):
            if nums[idx] <= pivot:
                nums[small + 1], nums[idx] = nums[idx], nums[small + 1]
                small += 1
                large += 1
            elif nums[idx] > pivot:
                large += 1

            # already comparep all n-1 element, swap the pivot to the mid and divide the list
            if idx == len(nums) - 2:
                nums[-1], nums[small + 1] = nums[small + 1], nums[-1]
    

        return self.QuickSort(nums[:small + 1]) + self.QuickSort(nums[small + 1:])


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