n=int(input("Enter  the no. of elements"))
c=[]
for i in range(1,n+1):
    print("Enter the",i,"charactor")
    i=input()
    l=len(i)
    while(l!=1):
        item("singel charactor")
        l=len(i)
    c.append(i)
strng=""
for i in c:
    strng=strng+i
print("string",strng)
