class Solution(object):
    def longestCommonPrefix(self, strs):
        strs_length = [len(i) for i in strs]
        common = [i for i in strs[0]][:min(strs_length)]
        
        for s in strs[1:]:
            for idx, a in enumerate(s):
                try:
                    if a == common[idx]:
                        pass
                    else:
                        common = common[:idx]
                except IndexError:
                    pass
        if len(common) == 0:
            return ""
        else:
            return ''.join(common)
                
        