class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n):
            # 끝부터 시작.. 
            idx = -(i+1)
            
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
            
        # 모든 숫자가 9
        return [1] + digits
        