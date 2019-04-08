myGakusekiNum = 55
b = (myGakusekiNum+100)*2
ans = 0

for x in range(3000):
    if (-x**2 + b*x - 5000) > 0:
        print(-x**2 + b*x - 5000,x)
        ans+=1

print(str(ans) + "個")