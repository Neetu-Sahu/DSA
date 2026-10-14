class Solution(object):
    def singleNumber(self, nums):
        d = {}
        ans = []

        for b in nums:
            if b in d:
                d[b] += 1
            else:
                d[b] = 1

        for a, b in d.items():
            if b == 1:
                ans.append(a)

        return ans