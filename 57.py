ab,cd=map(int,input().split())
l=list(map(int,input().split()[:ab]))
count=0
for i in l:
    if(i==cd):
        count=count+1
print(count)           
