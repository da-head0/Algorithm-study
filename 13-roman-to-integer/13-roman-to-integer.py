class Solution(object):
    def romanToInt(self, s):
        value_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        answer = 0
        
        for (idx, num) in enumerate(s):
            if idx < len(s)-1:
                if (num == 'I') and (s[idx+1] in ['V', 'X']):
                    answer -= value_dict[num]
                elif (num == 'X') and (s[idx+1] in ['L', 'C']):
                    answer -= value_dict[num]
                elif (num == 'C') and (s[idx+1] in ['D', 'M']):
                    answer -= value_dict[num]
                else:
                    answer += value_dict[num]
            else:
                answer += value_dict[num]
                
        return answer
        