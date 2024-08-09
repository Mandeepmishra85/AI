#Wap to find maximum and minimum number
a = [2,5,4,5,4,3,87,53,0,67]
temp=a[0]
for i in a:
    if i>temp:
        temp=i
print(f'the greatest number is => {temp}')
for i in a:
    if i<temp:
        temp=i
print(f'the minimum number is => {temp}')
