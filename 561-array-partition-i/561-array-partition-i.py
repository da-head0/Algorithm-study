class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        pair = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if i%2 ==0:
                sum += n
        
        return sum