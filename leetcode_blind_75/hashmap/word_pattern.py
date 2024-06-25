class Solution:
    def next_char(self,c):
        return chr(ord(c) + 1)

    def wordPattern(self, pattern: str, s: str) -> bool:
        s_word_list = s.split(" ")
        if len(pattern) != len(s_word_list):
            return False

        s_word_dict = dict()
        last_char = "a"
        for word in s_word_list:
            if not s_word_dict.get(word):
                s_word_dict[word] = last_char
                last_char = self.next_char(last_char)

        s_pattern = ""
        for word in s_word_list:
            s_pattern += s_word_dict[word]

        pattern_word_dict = dict()
        last_char = "a"
        for word in pattern:
            if not pattern_word_dict.get(word):
                pattern_word_dict[word] = last_char
                last_char = self.next_char(last_char)

        new_pattern = ""
        for word in pattern:
            new_pattern += pattern_word_dict[word]
        
        
        return new_pattern  == s_pattern