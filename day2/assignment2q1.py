a=int(input("Enter the number to be identified = "))
if a%2==0:
    print(a,"is even")
else:
    print(a,"is odd")
if a>1:    
    for i in range(2,a):
        if a%i==0:
            print(a,"is not prime")
            break
    else:
        print(a,"is prime")
l=len(str(a))        
for i in range(l%2):
    if str(a)[i]!=str(a)[l-1-i]:
        print(a,"is not palidrome")
        break
else:
     print(a,"is palidrome")
s=str(a)
r=0
for i in range(l):
    r=r+int(s[i])**3
    if r==int(s):
        print(a,"is an armstrong number")
else:
    print(a,"is not an armstrong number")          
