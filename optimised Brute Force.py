class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        ans = 0

        for i in range(n):
            min_h = heights[i]

            for j in range(i, n):
                min_h = min(min_h, heights[j])
                width = j - i + 1
                ans = max(ans, min_h * width)

        return ans


heights = [2, 1, 5, 6, 2, 3]
obj = Solution()
print("Largest Rectangle Area:", obj.largestRectangleArea(heights))
