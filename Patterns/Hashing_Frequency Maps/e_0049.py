from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            key = tuple(count)
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())

'''
Time Complexity:O(n.m), where n is the number of strings and m is the maximum string length. Creating each frequency array takes O(m + 26).
Space Complexity: \(O(n \cdot 26)\) for the frequency keys, plus storage for the grouped strings.
More precisely, including the input strings in the output, total auxiliary and output storage is O(n.26 + S), where S is the total number of characters across all strings.
'''
