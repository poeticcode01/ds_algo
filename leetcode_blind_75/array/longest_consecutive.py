from collections import defaultdict
def find_longest_consecutive(input_arr):
    input_len = len(input_arr)
    if input_len == 0:
        return 0
    
    elem_map = defaultdict(bool)
    for itm in input_arr:
        elem_map[itm] = True
    
    cur_max_len = 1
    for itm in input_arr:
        strt = itm
        nxt = itm + 1
        while elem_map.get(nxt):
            elem_map[nxt] = False
            nxt +=1
        cur_max_len = max(cur_max_len,nxt-strt)
    return cur_max_len

if __name__ == "__main__":
    input_arr = [100, 4, 200, 1, 3, 2]
    input_arr = [100]
    input_arr = [1,1,1]
    print("Length of longest consecutive element is: ",find_longest_consecutive(input_arr))
    