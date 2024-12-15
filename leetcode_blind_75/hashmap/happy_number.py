class Solution:
    def isHappy(self, n: int) -> bool:


        def get_sum_of_squares(x):
            ans = 0
            while x:
                rem = x%10
                ans += rem*rem
                x = x//10
            return ans


        cur_num = n
        visited = set()
        visited.add(cur_num)
        while True:
            new_num = get_sum_of_squares(cur_num)

            if new_num == 1:
                return True
            if new_num in visited:
                return False
            else:
                visited.add(new_num)
                cur_num = new_num