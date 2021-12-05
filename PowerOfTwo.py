#power of 2 
i=0
pow=1
n=int(input("enter the number which we want power of two : "))
if(0<=n<31):
 while(i<=n):
    
    if i==0:
        print("power of 2^0 is : 1")
    else:
       pow=pow*2
       print("power of 2 rest ",i,"is:",pow)
   
    i=i+1
else:
    print("enter value bitween 0 to 30")    