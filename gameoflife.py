class Grid:
    def __init__(self,size):
        self.size = size
        self.grid=[[0]*(self.size+2)]*(self.size+2)


    def count_nbr(self,row,col):
        count=0
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if self.grid[i][j]==1:                        
                    count+=1
        if self.grid[row][col]==1:
            return count-1
        else:
            return count
        

    def next_move(self):
        n_grid=[[0]*(self.size+2)]*(self.size+2)
        for i in range(1,(self.size+1)):
            for j in range (1,(self.size+1)):
                nbr=self.count_nbr(i,j)
                
                if self.grid[i][j]==0 and nbr==3:
                    n_grid[i][j]=1
                elif self.grid[i][j]==1 and (nbr==0 or nbr==1 or nbr>=4):
                    n_grid[i][j]=0
                elif self.grid[i][j]==1 and (nbr==2 or nbr==3):
                    n_grid[i][j]=1
                else:
                    n_grid[i][j]=0
                if i==0 and j==1:
                    print(nbr)
        print(n_grid)
    
n=int(input("enter size :"))
lis=[[0]*(n+2)]*(n+2)
for i in range(1,n+1):
    for j in range(1,n+1):
        lis[i][j]=int(input("enter value : "))
    print("next row starts now")
        
g=Grid(n)
g.grid=lis
g.next_move()
g.next_move()