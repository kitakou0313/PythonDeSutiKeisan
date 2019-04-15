diceNumList = [1,2,3,4,5,6]
ans = 0

for x in diceNumList:
	for y in diceNumList:
		for z in diceNumList:
			for v in diceNumList:
				n = x*1000+y*100+z*10+v
				if n%45 == 0:
					ans+=1
					print(x,y,z,v)
print(ans)
