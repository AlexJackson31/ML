n=int(input("Enter no. of rows for first matrix:"))
m=int(input("Enter no. of columns for first matrix:"))
p=int(input("Enter no. of rows for second matrix:"))
lst1=[]
lst2=[]
if p!=n:
    print("Invalid no. of rows")
    p=int(input("Enter valid no. of rows:"))
q=int(input("Enter no. of columns for second matrix:"))
for i in range(0,n):
    for j in range(0,m):
        n=int(input("Enter a value:"))
        #lst1[i][j].add(n)
print(lst1)
