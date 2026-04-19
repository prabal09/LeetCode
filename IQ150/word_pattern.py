class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # print(words)
        if len(words) != len(pattern):
            return False
        
        map_words_to_ch = {}
        map_ch_to_words = {}

        for word,ch in zip(words,pattern):
            print(word,ch)
            print(map_words_to_ch,map_ch_to_words)
            if word in map_words_to_ch and map_words_to_ch[word] != ch:
                return False
            if ch in map_ch_to_words and map_ch_to_words[ch] != word:
                return False 
            map_words_to_ch[word] = ch
            map_ch_to_words[ch] = word
        return True