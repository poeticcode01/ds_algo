from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_freq = defaultdict(int)
        magazine_freq = defaultdict(int)

        for itm in ransomNote:
            ransom_note_freq[itm] +=1

        for itm in magazine:
            magazine_freq[itm] +=1

        for key,val in ransom_note_freq.items():
            if magazine_freq[key] < val:
                return False

        return True