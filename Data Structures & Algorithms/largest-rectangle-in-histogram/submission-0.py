class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        areaM = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                areaM = max(areaM, height*(i - index))
                start = index
            stack.append([start, h])

        for i, h in stack:
            areaM = max(areaM, h*(len(heights) - i))
        
        return areaM

# Time Complexity: O(n)
# Space Complexity: O(n)