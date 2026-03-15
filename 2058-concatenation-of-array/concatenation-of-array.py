class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0]*2*n
        i = 0
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
            i = i + 1
        print("output is", ans)
        return ans
