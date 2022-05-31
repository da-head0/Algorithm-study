class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        # 인덱스와 숫자
        for index, num in enumerate(nums):
            
            # 목표값에서 지금 넘버를 뺀 값이 딕셔너리에 있다면
            if target - num in nums_map:
                return[nums_map[target - num], index]
            
            nums_map[num] = index
