import random
import datetime
o = datetime.datetime.now().second

x = random.randint(1,10)
a = int(input('Sanjarbek son kiriting!!!'))
urinish = 0
while a != x:
    if a%2==0:
        if a>x:
            x+=2
        elif a<x:
            x-=2
        qiymat = 'Juft'
        urinish += 1
    else:
        if a>x:
            x+=1
        elif a<x:
            x-=1
        qiymat = 'Toq'
        urinish += 1
y = datetime.datetime.now().second
print(f'Qoyil komyuter biz oylagan {x} {qiymat} sonini {urinish} ta urinishda {y-o} sekundda  topdi.')
