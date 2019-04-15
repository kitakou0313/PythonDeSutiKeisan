myGakusekiNum = 55
b = (myGakusekiNum+100)*2
ans = 0

for x in range(3000):
    if (-1*(x**2) + b*x - 5000) > 0:
        ans+=1

print(str(ans) + "個")