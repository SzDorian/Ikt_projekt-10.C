
#Első feladat
'''
a = input('Milyen napod van ?')

if a == "Jó":
    print('Örülök')
elif a == "Rossz":
    print('Az baj')
else:
    print('Nem válaszoltál!!')       
'''
#----------------------------------

#Második feladat
'''
szam1 = int(input('Kérek egy számot:'))

if szam1 % 2:
    print('A szám páratlan')
else:
    print('A szám páros')    
'''    
#--------------------------------------

#Harmadik feladat
'''
gondolt = 3

szam1 = int(input('Kérek egy számot 1 és 5 között:'))

if gondolt == szam1:
    print('Egyenlő a két szám')
elif gondolt < szam1:
    print('A tippelt szám nagyobb ') 
elif gondolt > szam1:
    print('A gondolt szám nagyobb')      
'''
#----------------------------------------------------
#----------------------------------------------------

#Első feladat

#1Feladat
"""
for paros in range(11):
    if paros % 2 ==  0:
        print(paros)"""

#2Feladat
"""
for x in range(1, 11):
    x -=11
    print(abs(x))"""

#3Feladat
"""
for x in range(1, 11):
    if x % 2 == 0:
        x -=11
        print(abs(x))"""

#4Feladat
szo = str(input("Kérek egy szót "))
ker = int(input("Hányszor? "))

for j in range(ker):
    print(szo)

