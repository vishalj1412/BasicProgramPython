#gate name from user 
str="Hello <<UserName>> How are you?"
name=input("Enter the name : ")
if len(name) > 3:
 print(str.replace("<<UserName>>",name))
 
else:
    print("enter name has minimum 3 character")  