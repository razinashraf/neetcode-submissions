class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        folder = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in folder:
                return [folder[diff],i]
            folder[n] = i