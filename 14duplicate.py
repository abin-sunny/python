n=input("Enter a number")
n=list(map(int,n.split()))
d=[]
for i in n:
    if(i not in d):
        d.append(i)
print(d)
