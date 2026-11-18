
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        ans = 0
        n = len(heights)

        for i in range(n + 1):
            curr = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > curr:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                ans = max(ans, h * width)

            if i < n:
                stack.append(i)

        return ans


heights = [2, 1, 5, 6, 2, 3]
obj = Solution()
print("Largest Rectangle Area:", obj.largestRectangleArea(heights))
