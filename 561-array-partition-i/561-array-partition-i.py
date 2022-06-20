class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        pair = []
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum