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
    def lengthOfLongestSubstring2(self, s):
        tmp_str = ""
        max_count = 0
        for idx in range(0, len(s)):
            if(s[idx] not in tmp_str):
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

