n=int(input())
m=int(input())
f=0
q=0
for i in range(1,n):
    if(n%i==0):
        f=f+i
for j in range(1,m):
    if(m%j==0):
        q=q+j
if (f==m and q==n):
    print("Amicable")
else:
    print("Not Amicable")