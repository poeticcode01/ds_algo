from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        ans = []
        word_len = len(words)
        while i < word_len:
            cur_width = 0
            j = i
            cur_word_list = []
            while j < word_len and cur_width < maxWidth:
                temp_len = len(words[j])
                if cur_width == 0:
                    cur_word_list.append(words[j])
                    cur_width += temp_len
                    j +=1
                    continue
                else:
                    if cur_width + temp_len + 1 <= maxWidth:
                        cur_word_list.append(words[j])
                        cur_width += (temp_len+1)
                        j +=1
                        continue
                    else:
                        break
            ans.append(cur_word_list)
            i = j

        final_ans = []
        for ind,cur_line in enumerate(ans):
            # print(ind,cur_line)
            space_slot = len(cur_line)-1
            word_width = 0
            for word in cur_line:
                word_width += len(word)

            total_space_width = maxWidth - word_width
            if space_slot >= 1:
                each_space_width = total_space_width//space_slot
                rem_space_width = total_space_width%space_slot
            else:
                each_space_width = 0
                rem_space_width = total_space_width



            each_space_slot = " "*each_space_width
            if rem_space_width == 0:
                if ind + 1  == len(ans):
                    # print("last_line",cur_line)
                    temp = ""
                    for word in cur_line:
                        if temp == "":
                            temp +=word
                        else:
                            temp = temp + " " + word
                    rem_space = maxWidth - len(temp)
                    temp = temp + " "*rem_space
                    final_ans.append(temp)
                else:
                    temp = ""
                    for word in cur_line:
                        if temp == "":
                            temp +=word
                        else:
                            temp = temp + each_space_slot + word
                    final_ans.append(temp)
            else:
                if ind + 1  == len(ans):
                    # print("last_line",cur_line)
                    temp = ""
                    for word in cur_line:
                        if temp == "":
                            temp +=word
                        else:
                            temp = temp + " " + word
                    rem_space = maxWidth - len(temp)
                    temp = temp + " "*rem_space
                    final_ans.append(temp)
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
                    final_ans.append(temp)
        return final_ans