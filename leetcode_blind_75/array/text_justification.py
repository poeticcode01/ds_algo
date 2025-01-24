from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        
        self.word_len = len(words)
        self.words = words
        self.maxWidth = maxWidth

        wordsPerline = self.packWordsPerline()
        

        self.final_ans = []
        for ind,cur_line in enumerate(wordsPerline):
            # print(ind,cur_line)
            each_space_width,rem_space_width = self.getSpaceWidthPerSlot(cur_line)
    
            if ind+1 == len(wordsPerline):
                self.handleLastLine(cur_line)   
            else:
                self.hanldeNonLastLine(cur_line,each_space_width,rem_space_width)
                

            
        return self.final_ans
    def packWordsPerline(self) -> List[str]:
        ans = []
        i = 0
        while i < self.word_len:
            cur_width = 0
            cur_word_list = []
            while i < self.word_len and cur_width < self.maxWidth:
                temp_len = len(self.words[i])
                if cur_width == 0:
                    cur_word_list.append(self.words[i])
                    cur_width += temp_len
                    i +=1
                    continue
                else:
                    if cur_width + temp_len + 1 <= self.maxWidth:
                        cur_word_list.append(self.words[i])
                        cur_width += (temp_len+1)
                        i +=1
                        continue
                    else:
                        break
            ans.append(cur_word_list)
        return ans
    
    def getSpaceWidthPerSlot(self,cur_line) ->(int,int): # type: ignore
        space_slot = len(cur_line) - 1
        word_width = 0
        for word in cur_line:
            word_width += len(word)

        total_space_width = self.maxWidth - word_width
        if space_slot >= 1:
            each_space_width = total_space_width//space_slot
            rem_space_width = total_space_width%space_slot
        else:
            each_space_width = 0
            rem_space_width = total_space_width

        return each_space_width,rem_space_width

    def handleLastLine(self,cur_line):
        temp = ""
        for word in cur_line:
            if temp == "":
                temp +=word
            else:
                temp = temp + " " + word
        rem_space = self.maxWidth - len(temp)
        temp = temp + " "*rem_space
        self.final_ans.append(temp)

    def hanldeNonLastLine(self,cur_line,each_space_width,rem_space_width):
        each_space_slot = " "*each_space_width
        if rem_space_width == 0:
            temp = ""
            for word in cur_line:
                if temp == "":
                    temp +=word
                else:
                    temp = temp + each_space_slot + word
            self.final_ans.append(temp)
        else:
            temp = ""
            for word in cur_line:
                if temp == "":
                    temp +=word
                else:
                    if rem_space_width > 0:
                        temp = temp + each_space_slot + " " + word
                        rem_space_width -=1
                    else:
                        temp = temp + each_space_slot +  word
            temp = temp + " "*rem_space_width
            self.final_ans.append(temp)

    