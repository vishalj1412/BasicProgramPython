import random
#Flip the coin and check it is Head or Tail
n=int(input("enter number of time you want flip the coin: "))
head=0
tail=0
for i in range(n):
 if random.random() < 0.5:
    head+=1
 else:
    tail+=1

PercentageOfHead=(head*100)/n
print(PercentageOfHead)

percentageOfTail=(tail*100)/n
print(percentageOfTail)
