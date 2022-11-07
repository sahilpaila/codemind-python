n=int(input())
large=0
rem=0
while n:
    rem=n%10
    n=n//10
    if(rem>=large):
        large=rem
    else:
        rem=rem
print(large)