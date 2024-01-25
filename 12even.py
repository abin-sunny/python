n=input("Enter a strng")
n=list(map(int,n.split(",")))
e=[item for item in n if (item%2==0)]
print(e)
