from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0]*26
            for ch in s:
                # print(ch)
                count[ord(ch)-ord('a')] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
        # print(list(anagrams_dict.values()))
        return list(anagrams_dict.values())