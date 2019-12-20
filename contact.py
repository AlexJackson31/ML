import csv
#import pandas
import os
current_dir=os.path.dirname(__file__)
fname=os.path.join(current_dir,"Contact_Book.csv")

fields=['Name','Phone no.','Email','Address']
rows=[]
lst=[]
name=input("Enter the name:")
lst.append(name)
phone=input("Enter the phone no:")
lst.append(phone)
email=input("Enter the email address:")
lst.append(email)
add=input("Enter the address:")
lst.append(add)
rows.append(lst)

#df=pandas.read_csv(fname)
with open(fname,"a+") as file:
    csvwriter=csv.writer(file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #csvwriter.writerow(fields)
    csvwriter.writerows(rows)

print("1.Name\n2.Phone no.\n3.Email")
n=int(input("Choose the parameter to search:"))
if n==1:
    with open(fname,"r") as file:
        n=input("Enter the name:")
        reader = csv.reader(file)
        for row in reader:
            for field in row:
                if n==field:
                    print(row)  
        
elif n==2:
    with open(fname,"r") as file:
        n=input("Enter the phone no:")
        reader = csv.reader(file)
        for row in reader:
            for field in row:
                if n==field:
                    print(row)   

else:
    with open(fname,"r") as file:
        n=input("Enter the email address:")
        reader = csv.reader(file)
        for row in reader:
            for field in row:
                if n==field:
                    print(row)  
        
