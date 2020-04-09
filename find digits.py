n=int(input(":"))
cnt=0
x=str(n)
a=n
for i in range(len(x)):
    r=a%10
    a=a//10
    if(r!=0):
        if(n%r)==0:
            cnt+=1
print(cnt)
