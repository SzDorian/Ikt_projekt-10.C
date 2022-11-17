#Első feladat
'''
szam = 1
while szam <=20:
    if szam % 2 == 0:
        print(szam,"páros")
        szam += 1
    elif szam % 2 == 1:
        print(szam,"páratlan")
        szam += 1
'''
#--------------------------------------------
#Második feladat
'''
list = []
szam = int(input("Kérek egy számot: "))
szam.append(list)
szam = 0
for a in list:
    szam += 1
    avg = szam / len(list)
        
print("A szám átlaga:",szam)
'''
#HARMADIK FELADAT
'''
also = int(input("Alső szám: "))
felso = int(input("Felső szám: "))

list = range(also,felso+1)
sum = 0
i = 0

for x in list:
    sum = sum + x
    i += 1

print(sum, sum/i)
'''
#Negyedik feladat
'''
szam1 =1
while szam1 <= 5:
    print(szam1)
    szam1 += 1"""
'''
#Ötödik feladat
'''
n = 1
list = []
while True:
    n = int(input("Kérek egy számot: "))
    n += 1
    list.append(n)
    if n != "":
        ossz = sum(n)
        print(ossz)
'''        