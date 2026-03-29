class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
               d[num] = 1 + d.get(num, 0)
        dic = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        res = []
        i = 0
        for key, values in dic.items():
            if i < k:
                res.append(key)
                i += 1
        return (res)

# Time Complexity: O(nlogn)
# Space Complexity: O(n)