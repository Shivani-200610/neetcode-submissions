class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i,n in enumerate(nums):
            if (target - n) in data:
                return [ data[target-n] , i ]
            data[n] = i

            
                

            
        