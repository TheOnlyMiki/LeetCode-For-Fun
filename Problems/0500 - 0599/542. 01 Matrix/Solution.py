class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        cols1, cols2 = range(n), range(n-1, -1, -1)
        maximum = m + n
        record1 = [maximum]*(n+1)
        record2 = [maximum]*(n+1)
        temp1 = temp2 = pre_i = None
    
        for i in range(m):
            record2[:n] = mat[i]
            for j in cols1:
                if mat[i][j] > 0:
                    mat[i][j] = record2[j] = min(record1[j], record2[j-1]) + 1

            record1[:] = record2[:]
        
        record1 = [maximum]*(n+1)
        for i in range(m-1, -1, -1):
            record2[:n] = mat[i]
            for j in cols2:
                if mat[i][j] > 0:
                    mat[i][j] = record2[j] = min(mat[i][j], min(record1[j], record2[j+1]) + 1)

            record1[:] = record2[:]
        
        return mat

        # Option 1 - No idea why it was wrong.
        """
        m, n = len(mat), len(mat[0])
        cols = range(n)
        maximum = m + n
        record1 = [maximum]*(n+1)
        record2 = [maximum]*(n+1)
        pre_i = cur_i = pre_j = cur_j = next_i = next_j = None
    
        for i in range(m):
            record2[:n] = mat[i]
            for j in cols:
                if mat[i][j] > 0:
                    mat[i][j] = record2[j] = min(record1[j], record2[j-1]) + 1
                
                pre_i, cur_i, pre_j, cur_j, next_i, next_j = i-1, i, j-1, j, i, j
                while next_i >= 0 and next_j >= 0:
                    while pre_i >= 0 and mat[pre_i][next_j] > mat[cur_i][next_j] + 1:
                        mat[pre_i][next_j] = mat[cur_i][next_j] + 1
                        cur_i = pre_i
                        pre_i -= 1

                    while pre_j >= 0 and mat[next_i][pre_j] > mat[next_i][cur_j] + 1:
                        mat[next_i][pre_j] = mat[next_i][cur_j] + 1
                        cur_j = pre_j
                        pre_j -= 1

                    pre_i, pre_j = next_i-1, next_j-1
                    cur_i, cur_j = pre_i+1, pre_j+1
                    next_i -= 1
                    next_j -= 1

            record1[:] = record2[:]
        
        return mat
        """
