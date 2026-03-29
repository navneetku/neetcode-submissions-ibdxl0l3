class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]

# Time Complexity: O(n)
# Space Complecity: O(n)