n=int(input())
rev=0
while(n!=0):
    rev=n % 10
    n=n // 10
    print(rev,end='')