import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph  = re.sub(r'[^\w]', ' ', paragraph)
        word_dict = {}
        word_list = [x.lower() for x in paragraph.split()]
        for word in word_list:
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        for b in banned:
            if b in word_dict:
                del word_dict[b]
        sorted_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
        return(sorted_list[0][0])
            
            