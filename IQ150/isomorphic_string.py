class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapST, mapTS = {}, {}

        for char_s, char_t in zip(s, t):
            # Check if mapping from s to t is consistent
            if char_s in mapST and mapST[char_s] != char_t:
                return False
            
            # # Check if mapping from t to s is consistent
            if char_t in mapTS and mapTS[char_t] != char_s:
                return False

            # Establish the mapping
            mapST[char_s] = char_t
            mapTS[char_t] = char_s
        # print(mapST,mapTS)
        return True
