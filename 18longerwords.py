a=input("Enter the list with comma")
l=a.split(',')
n=int(input("Enter a number"))
print("numbers more than enterd charactor are",)
[print(i) for i in l if(len(i)>n)]
