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

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
    # answer in intuition
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max_count = 1
        for base in range(0, len(s)):
            tmp_str = s[base]
            count = 1           

            for idx in range(base + 1, len(s)):
                if(s[idx] not in tmp_str):
                    tmp_str += s[idx]
                    count += 1
                    max_count = max(max_count, count)
                else:
                    break         
        return max_count
    # O(n) solution  
    # the key conception: when encounter the same character 'x' already apeared in tmp_str,
    #   we reassign the tmp_str from the x's index + 1, and add 'x' in the tail 
    def lengthOfLongestSubstring2(self, s):
        tmp_str = ""
        max_count = 0
        for idx in range(0, len(s)):
            if s[idx] not in tmp_str:
                tmp_str += s[idx]
            else:
                idx_samechar = tmp_str.index(s[idx])
                tmp_str = tmp_str[idx_samechar + 1:] + s[idx]
            max_count = max(max_count, len(tmp_str))
        return max_count

# 9. Palindrome Number
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
#   -121: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
#
#   Note: This solution exceed limit time after submit to leetcode online, check this later.
# 10/14 update: 
#   TODO: After checking others discusstion, this probelm can be solved in O(N)
#
    def IsStrPalindrome(self, s:str) -> bool:
        if s == s[::-1]:
            return True
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        tmp_str = max_str = ""
        
        for idx in range(len(s)):
            for idx2 in range(idx, len(s)):
                tmp_str = s[idx:idx2 + 1]
                if self.IsStrPalindrome(tmp_str) and len(max_str) < len(tmp_str):
                    max_str = tmp_str
        return max_str

# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre_str = ""
        for idx in range(1, len(strs[0]) + 1):
            tmp_str = strs[0][:idx]
            for num in range(1, len(strs)):
                if tmp_str != strs[num][:idx]:
                    return pre_str
            pre_str = tmp_str
        return pre_str

# 13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
    def romanToInt(self, s: str) -> int:
        if s == "":
            return 0
        dicRom = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = 0
        
        for idx in range(len(s) - 1):                
            if dicRom[s[idx]] >= dicRom[s[idx + 1]]:
                total += dicRom[s[idx]]
            else: 
                total -= dicRom[s[idx]]
        return total + dicRom[s[len(s) - 1]]

# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
    def isValidParentheses(self, s: str) -> bool:
        list_left = ['(', '[', '{'] 
        list_right = [')', ']', '}'] 
        idx = 0
        tmp_list = list(s)
        while idx < (len(tmp_list)):
            if tmp_list[idx] in list_right:
                if idx == 0:
                    return False
                if tmp_list[idx - 1] == list_left[list_right.index(tmp_list[idx])]:
                    tmp_list.pop(idx)
                    tmp_list.pop(idx - 1)
                    idx -=1
                    continue
            idx += 1
        return tmp_list == []

    # 10/12 update: try using dictionary
    def isValidParentheses2(self, s: str) -> bool:
        dic_paren = { ')':'(', ']':'[',  '}':'{' }
        list_stack = []

        for each_paren in s:
            if each_paren in dic_paren.values():
                list_stack.append(each_paren)
            elif each_paren in dic_paren:
                if list_stack == []:
                    return False
                if dic_paren[each_paren] != list_stack.pop():
                    return False
        return list_stack == []

# 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
# Custom Judge:
# The judge will test your solution with the following code:
#
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp_list = []
        count = 0
        for num in nums:
            if num not in tmp_list:
                count += 1
                tmp_list.append(num)
        
        return count

# 53. Maximum Subarray - easy
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Note: Using Dynamic Programing!!
#  
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum_for_curr = nums[0]
        idx = 1
        maxsum = nums[0]
        while idx < len(nums):
            if maxsum_for_curr > 0:
               maxsum_for_curr = maxsum_for_curr + nums[idx]
            else:
               maxsum_for_curr = nums[idx]

            maxsum = max(maxsum, maxsum_for_curr)
            idx += 1
        return maxsum

# 58. Length of Last Word
# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
    def lengthOfLastWord(self, s: str) -> int:
        currword = 0
        lastword = 0
        for char in s:
            if char == ' ':      
                currword = 0
            else:
                currword += 1
            if currword != 0:
                lastword = currword
        return lastword


# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
    def addBinary(self, a: str, b: str) -> str:
        list_a = list(a)
        list_b = list(b)
        carry = 0
        sum = ''
        while list_a or list_b or carry:
            if list_a:
                carry += int(list_a.pop())
            if list_b:
                carry += int(list_b.pop())
            
            sum = str(carry % 2) + sum
            carry = carry // 2
        
        return sum

# 69. Sqrt(x)
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
# Example :
#     Input: x = 8
#     Output: 2
#     Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
#
    def mySqrt(self, x: int) -> int:
        root = 0
        while True:
            if root * root > x:
                return root - 1
            root += 1

# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:
#     Input: n = 2
#     Output: 2
#     Explanation: There are two ways to climb to the top.
#     1. 1 step + 1 step
#     2. 2 steps
# Example 2:
#     Input: n = 3
#     Output: 3
#     Explanation: There are three ways to climb to the top.
#     1. 1 step + 1 step + 1 step
#     2. 1 step + 2 steps
#     3. 2 steps + 1 step
# 
    def climbStairs(self, n: int) -> int:
        pre = 0
        curr = 1
        for idx in range(n):
            curr = curr + pre
            pre = curr - pre
        return curr
        # recursive
        if n <= 2:
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2) 

# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
#   representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
#   and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
# nums1.length == m + n
# nums2.length == n
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for idx in range(n):
            nums1[m + idx] = nums2[idx]

        no_swap = True
        for idx in range(m + n - 1, 0 , -1):
            for bubble in range(idx):
                if nums1[bubble] > nums1[bubble + 1]:
                    nums1[bubble], nums1[bubble + 1] = nums1[bubble + 1], nums1[bubble]
                    no_swap = False
            if no_swap:
                break
        return 
    
#977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, 
#   return an array of the squares of each number sorted in non-decreasing order.
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        opt = [None for num in nums]
        for idx in range(len(nums)):
            if abs(nums[left]) > abs(nums[right]):
                opt[idx] = nums[left] ** 2
                left += 1
            else:
                opt[idx] = nums[right] ** 2
                right -= 1
        return opt[::-1]
