class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_element = list(jewels)
        for s in stones:
            if s in jewels_element:
                count += 1
        return count
                
        