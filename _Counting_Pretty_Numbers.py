for i in range(int(input())):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        y=i%10
        if(y==2 or y==3 or y==9):
            c+=1
    print(c)