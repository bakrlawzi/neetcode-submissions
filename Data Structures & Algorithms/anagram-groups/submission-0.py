from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        result.append([strs[0]])
        visible = False
        for i in range(1,len(strs)):
            visible = False
            for j in range(len(result)):
                temp_hash_1 = Counter(strs[i])
                temp_hash_2 = Counter(result[j][0])
                if temp_hash_1 == temp_hash_2:
                    result[j].append(strs[i])
                    visible = True
                    break
            if visible==False:
                temp = []
                temp.append(strs[i])
                result.append(temp)
        return result