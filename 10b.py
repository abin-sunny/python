vowels=['a','A','e','E','i','I','o','O']
s1="hello welcome to mace"
s2=list(s1)
print(s2)
v=[i for i in s2 if(i in vowels)]
print(v)
