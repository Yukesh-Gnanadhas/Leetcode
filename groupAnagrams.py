class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using hash map
        grp={}
        for char in strs:
            sorted_char = "".join(sorted(char))
            if sorted_char in grp:
                grp[sorted_char].append(char)
            else:
                grp[sorted_char] = [char]

        return list(grp.values())
