class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            dct = [0] * 26
            for c in s:
                dct[ord(c) - ord('a')] += 1
            d[tuple(dct)].append(s)
        return list(d.values())

# Time Complexity: O(m*n)
# Space Complexity: O(m)