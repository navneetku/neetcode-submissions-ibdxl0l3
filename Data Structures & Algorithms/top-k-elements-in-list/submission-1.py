class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for key, value in d.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
# Time Complexity: O(n)
# Space Complexity: O(n)