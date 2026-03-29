class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sd, td = {}, {}
            for i in range(len(s)):
                if s[i] not in sd:
                    sd[s[i]] = 1
                else:
                    sd[s[i]] += 1
            for j in range(len(t)):
                if t[j] not in td:
                    td[t[j]] = 1
                else:
                    td[t[j]] += 1
        if td == sd:
            return True
        else:
            return False

# Time Complexity: O(n)
# Space Complexity: O(n)