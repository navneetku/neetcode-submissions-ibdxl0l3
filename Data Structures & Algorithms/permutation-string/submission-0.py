class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        maxMatch = 0
        for i in range(len(s1Count)):
            if s1Count[i] == s2Count[i]:
                maxMatch += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if maxMatch == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                maxMatch += 1
            elif s1Count[index] + 1 == s2Count[index]:
                maxMatch -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                maxMatch += 1
            elif s1Count[index] - 1 == s2Count[index]:
                maxMatch -= 1
            l += 1
        return maxMatch == 26

# Time Complexity: O(n)
# Space Complexity: O(1)
            