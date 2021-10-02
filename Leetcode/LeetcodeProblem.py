from typing import List


class Solution:
# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#  
# Date: 2021/09/23
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if(len(nums)) < 2:
            return None
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target:
                    #print(str(i) + " + " +  str(j) + " = " + str(target))
                    list_ans = [i, j]
                    return list_ans

# 66. Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
#
# Date: 2021/09/23
    def plusOne(self, digits: List[int]) -> List[int]:        
        if digits[-1] % 10 != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            if(len(digits) == 1):
                digits.insert(0, 1)
            else:                
                digits = self.plusOne(digits[:-1])
                digits.insert(len(digits), 0)
            return digits
# Date: 2021/09/24 
    def plusOne2(self, digits: List[int]) -> List[int]:        
        for i in range(len(digits)-1 , -1 , -1):
            if digits[i] != 9:
                digits[i] += 1 
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits
                else:
                    continue








