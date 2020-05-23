n=int(input("enter the lenghth of pattern"))
for i in range(n):
    print("*"*(n-i)+" "*(2*i+1)+"*"*(n-i))
for i in range(n):
    print("*"*(i+1)+" "*(n+4-i*2)+"*"*(i+1))  
