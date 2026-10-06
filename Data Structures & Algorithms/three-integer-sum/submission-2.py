from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        res = []
        
        for i in range(len(nums)):
            # Step 2: Skip duplicate elements for the first position
            if i > 0 and nums[i] == nums[i-1]:
                continue 
                
            current = nums[i]
            target = -current  # Step 3: Fixed the assignment and target calculation
            
            left = i + 1 
            right = len(nums) - 1 

            # Step 4: Two-pointer search
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers inward
                    left += 1
                    right -= 1
                    
                    # Skip duplicate elements for left and right positions
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total > target:
                    right -= 1  # Sum is too big, move the right pointer left
                else:
                    left += 1   # Sum is too small, move the left pointer right
                     
        return res  # Fixed the indentation here
