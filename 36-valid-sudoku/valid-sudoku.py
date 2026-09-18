class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        flag = 0

        # Check rows
        for i in range(9):
            hr = {}
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                hr[num] = hr.get(num, 0) + 1
                if hr[num] > 1:
                    flag = 1
                    break

        # Check columns
        for i in range(9):
            hf = {}
            for j in range(9):
                num = board[j][i]
                if num == ".":
                    continue
                hf[num] = hf.get(num, 0) + 1
                if hf[num] > 1:
                    flag = 1
                    break

        # Check boxes
        hb = {}
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                boxr = i // 3
                boxc = j // 3
                box = boxr * 3 + boxc
                if box not in hb:
                    hb[box] = {}
                hb[box][num] = hb[box].get(num, 0) + 1
                if hb[box][num] > 1:
                    flag = 1
        if flag == 1:
            return False
        else:
            return True