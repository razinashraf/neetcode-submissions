class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        p = [1]*n
        s = [1]*n
        
        
        for i in range(1,n):
            p[i] = nums[i-1] * p[i-1]
        for i in range(n-2,-1,-1):
            s[i] = nums[i+1] * s[i+1]
        for i in range(n):
            res[i] = p[i]*s[i]
        
        return res