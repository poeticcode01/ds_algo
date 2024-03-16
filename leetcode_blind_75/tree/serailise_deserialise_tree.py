# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = ""
        if not root:
            return ans
        # print(len(ans))
        ans = []
        dq = deque([root,"#"])
        ind = 0
        cur_level = []
        while dq:
            k = dq.popleft()
            if  k == "#" and not dq:
                break
            elif  k == "#":
                dq.append("#")
                ans.append(cur_level)
                cur_level = []
                continue
            
            if k:
                cur_level.append(str(k.val))       
            else:
                cur_level.append("#")
                continue
            dq.append(k.left)
            dq.append(k.right)
        ans = [ ",".join(cur_level) for cur_level in ans]
        ans = "|".join(ans)
        # print(ans)
        return ans



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data:
            data = data.split("|")
        # print(data)
        return self.createTree(data)

    def createTree(self,data):
        if len(data) == 0:
            return None
        data = [cur_level.split(",") for cur_level in data]
        cur_level_ind = 0
        root = None
        # print(data)
        while cur_level_ind < len(data):
            for ind, itm in enumerate(data[cur_level_ind]):
                if itm == "#":
                    data[cur_level_ind][ind] = None
                    continue
                node = TreeNode(int(itm))
                data[cur_level_ind][ind] = node
            cur_level_ind +=1

        cur_level = 0
        while cur_level < len(data) - 1:
            self.connectNodes(cur_level,data)
            cur_level +=1
        return data[0][0]
        

    def connectNodes(self, cur_level,data):
        run_ind = 0
        cur_level_data = data[cur_level]
        nxt_level_data = data[cur_level+1]
        for ind, itm in enumerate(cur_level_data):
            if not itm:
                continue
            itm.left = nxt_level_data[run_ind]
            itm.right = nxt_level_data[run_ind+1]
            run_ind +=2