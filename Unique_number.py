num=int(input())
a=list(map(int,str(num)))
if (len(a)==len(set(a))):
    print("Unique Number")
else:
    print("Not Unique Number")
    