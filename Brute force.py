
class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                h = min(heights[i:j+1])
                width = j - i + 1
                ans = max(ans, h * width)

        return ans


heights = [2, 1, 5, 6, 2, 3]
obj = Solution()
print("Largest Rectangle Area:", obj.largestRectangleArea(heights))
