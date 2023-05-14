import itertools 

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        minsum = num
        numlist = [s for s in str(num)]
        for nums in list(itertools.permutations(numlist, 4)):
            nums = ''.join(list(nums))
            for i in range(1,4):
                num1, num2 = int(nums[:i]), int(nums[i:])
                if num1 + num2 < minsum:
                    minsum = num1 + num2
        return minsum
