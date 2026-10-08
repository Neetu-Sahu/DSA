class Solution(object):
    def subarraySum(self, nums, k):
         #count=0

         #for i in range(0,len(nums)):
         #  total=0
         #  for j in range(i,len(nums)):
         #      total+=nums[j]

         #       if total==k:
         #          count+=1

         #return count

        count = 0
        curr_sum = 0
        prefix = {0: 1}

        for num in nums:
            curr_sum += num

            if curr_sum - k in prefix:
                count += prefix[curr_sum - k]

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

        return count
            
        