class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    z=board[i].count(board[i][j])
                    if z>1:
                        print(1)
                        return False
        for i in range(9):
            l=[]
            for j in range(9):
                
                if board[j][i] == ".":
                    continue
                else:
                    l.append(board[j][i])
                    #print(l)
            if len(set(l)) != len(l):
                print(2)
                return False
        l=[]

        for i in range(0,9,3):
            for j in range(9):
                s=board[j][i:i+3]
                l.append(s)
        for i in range(len(l)):
            for j in range(3):
        
                l.append(l[i][j])
        l=l[27:]
        for j in range(0,len(l),9):
            p=l[j:j+9]
            for i in p:
                if i!= ".":
                    z=p.count(i)
                    if z>1:
                        print(3)
                        return False
        return True
        

