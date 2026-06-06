'''
This file contains the implementation of the solution for LeetCode_120.
For more note, please refer to the LeetCode_120/Note.md file.
'''
from typing import List


class Solution:
    # This is the LeetCode Quesion 1 Solution. [Easy]
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        check = {}
        
        for i in range(len(nums)):
            left = target - nums[i]
            if left in check:
                return [check[left], i]
            check[nums[i]] = i
        return []
    
    # This is the LeetCode Quesion 217 Solution. [Easy]
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1 = nums
        if len(set(nums)) < len(nums1):
            return True
        else:
            return False
        
    # This is the LeetCode Quesion 242 Solution. [Easy]
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)
    
    # This is the LeetCode Quesion 49 Solution. [Medium]
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  
        check = {}
        for i in strs:
            
            key = "".join(sorted(i))

            if key not in check:
                check[key] = []
            check[key].append(i)
        return list(check.values())
    
    # This is the LeetCode Quesion 347 Solution. [Medium]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        checks = {}

        for i in nums:
            if i not in checks:
                checks[i] = 1
            else:
                checks[i] += 1

    # Sort by frequency
        def get_frequency(item):
            return item[1]

        sorted_items = sorted(
            checks.items(),
            key=get_frequency,
            reverse=True
        )

        # Get top k elements
        result = []

        for num, freq in sorted_items[:k]:
            result.append(num)

        return result
    
    # This is the LeetCode Quesion 238 Solution. [Medium]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]* len(nums)
        pos = pre = 1

        for i in range(len(nums)):
            ans[i] = pre
            pre *= nums[i]
        
        for i in range(len(nums) -1 , -1, -1):        
            ans[i] *= pos
            pos *= nums[i]
        return ans

    # This is the LeetCode Quesion 36 Solution. [Medium]
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = set()

        for i in range(9):
            for j in range(9):
                coordination = board[i][j]

                if coordination != ".":
                    if ((i, coordination) in check or
                        (coordination, j) in check or
                        (i // 3, j // 3, coordination) in check):
                        return False
                
                    check.add((i, coordination))
                    check.add((coordination, j))
                    check.add((i // 3, j // 3, coordination))
        return True