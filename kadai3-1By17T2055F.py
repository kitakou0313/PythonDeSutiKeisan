import itertools

aOver3Num = 0
abInNum = 0

for mozi in itertools.product("ab", repeat=8):
    if("".join(list(mozi)).count("a") >= 3):#aを3個以上含む場合、カウントアップ
        aOver3Num += 1
    if ("ab" in "".join(list(mozi))):#abを含む場合、カウントアップ
        abInNum+=1

print("aを3つ以上含むもの-",aOver3Num,"abを含むもの-",abInNum)
#一行で解く場合
print("aを3つ以上含むもの-",sum(1 for mozi in itertools.product("ab", repeat=8) if ("".join(list(mozi)).count("a") >= 3)),"abを含むもの-",sum(1 for mozi in itertools.product("ab", repeat=8) if ("ab" in "".join(list(mozi)))))
