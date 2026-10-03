from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) fast lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if 'num' is the absolute start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Keep counting the next consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Keep track of the maximum length found
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
