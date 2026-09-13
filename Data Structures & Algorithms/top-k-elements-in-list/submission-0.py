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
        sorted_folder = list(sorted_folder[-k:])
        result = []
        for k,v in sorted_folder:
            if (k,v) in sorted_folder:
                result.append(k)
        return result
        