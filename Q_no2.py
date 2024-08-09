#wap to sum digit
num=int(input("enter a digit:"))
sum=0;
while num>0:
    sum=sum + (num%10)
    num=num//10
print(sum)    
