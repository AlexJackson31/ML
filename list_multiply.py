lst1=[[1,2,3],[4,5,6],[7,8,0]]
lst2=[[3,7,5],[0,1,0],[1,9,8]]
c=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,len(lst1)):
    for j in range(0,len(lst2[0])):
        for k in range(0,len(lst2[0])):
            c[i][j]=c[i][j]+lst1[i][k]*lst2[k][j]
print(c)
