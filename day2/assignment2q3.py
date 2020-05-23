n=int(input("enter the lenghth of pattern"))
for i in range(n):
    print(" "*(i)+"*"+" "*(n+2-2*i)+"*")
for i in range(n):
    print(" "*(n-i-1)+"*"+" "*(2*i)+"*")    
