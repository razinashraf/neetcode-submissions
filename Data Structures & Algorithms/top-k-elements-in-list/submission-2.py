class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        folder = {}

        for i in nums:
            if i not in folder:
                folder[i] = 1
            else:
                folder[i] += 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for num,count in folder.items():
            buckets[count].append(num)
        
        result = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        