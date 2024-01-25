c=int(input("Enter current year"))
f=int(input("Enter future year"))
list=[]
list=[i for i in range(c,f) if i%4==0 and (i%400==0 or i%100!=0)]
print("leap year are : ,", list)
