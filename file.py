from datetime import datetime
msg=input("Enter the message:")
ty=input("Enter the type of message:")
now=datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
with open("log.txt","a+") as file:
    str="Message: "+msg+"\nType: "+ty+"\nCreated on: "+date_time+"\n"
    file.write("\n"+str)
    file.seek(0,0)
    print("File contents are:")
    line=file.read()
    print(line)



