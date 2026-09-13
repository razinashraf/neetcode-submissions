class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        folder = {}

        for i in nums:
            if i not in folder:
                folder[i] = 1
            else:
                folder[i] += 1
        
        sorted_folder = sorted(folder.items(),key = lambda x: x[1])
        result = [key for key, value in sorted_folder[-k:]]
        return result
        