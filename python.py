# Find odd and even number between the range and prime number
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=[]
d=[]
for x in range(a,b+1):
    if x%2==0:
        c.append(x)
    else:
        d.append(x)
print(c)
print(d)
for d in range (a,b):
    if d==0 or d==1:
        print(f"{d} is not  prime number")
    elif d>1:
        for k in  range(2,d):
            if  (d%k)==0:
                print(f"{d}  is not prime number")
                break
        else:
            print(f"{d} is prime number")
