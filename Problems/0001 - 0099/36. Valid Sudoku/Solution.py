class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        count = { num:{} for num in "123456789" }

        for i, x in enumerate(board):
            x_sub_boxes = i // 3

            for i_2, y in enumerate(x, start=9):
                if y != '.':
                    y_sub_boxes = i_2 // 3

                    if i in count[y] or i_2 in count[y] or (x_sub_boxes, y_sub_boxes) in count[y]:
                        return False
                    count[y][i] = count[y][i_2] = count[y][(x_sub_boxes, y_sub_boxes)] = None

        return True
