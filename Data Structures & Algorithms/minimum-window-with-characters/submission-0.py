class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countS, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float('infinity')
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1

            while have == need:
                if resLen > (r - l + 1):
                    res = [l, r]
                    resLen = r - l + 1
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float('infinity') else ""

# Time Complexity: O(n)
# Space Complexity: O(1)