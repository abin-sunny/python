n=int(input("Enter  the no. of elements"))
num=[]
print("Enter the numbers")
for i in range(1,n+1):
    item=int(input())
    num.append(item)
sm=[item for item in num if(item>min(num))]
print("second smallest number is",min(sm))
