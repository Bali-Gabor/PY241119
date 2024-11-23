# 2/1 feladat (Név10)

# for x in range(10):
#     print(f'{x+1}. Bali Gábor')


# 2/2 feladat (IsmétlésN)

# szoveg=input('Mit ismételjek?  ')
# n=int(input('Add meg az ismétlés számát!  '))
# for _ in range(n):
#     print(szoveg, end=' ')


# 2/3 feladat (Visszaszámol)

# import time
# import os

# n=10
# while n>0:
#     print(n, end='')
#     time.sleep(1)
#     os.system('cls')
#     n-=1
# print('Lejárt az idő!')


# 2/4 feladat (Név_mozog)

# import time, os

# nev=input('Kérlek add meg a neved!  ')
# for x in range(20):
#     print(nev, end='')
#     time.sleep(.3)
#     os.system('cls')
#     print(x*' ',end='')



# 2/5 feladat (Random_csillag)
# Nem megoldható
# 2/6 feladat (Randomszín)
# Nem megoldható


# 2/7 feladat (Négyzetszámok)

# for x in range(0,31):
#     print(x**2)


# 2/8 feladat (2hatványok)

# for x in range(0,31):
#     print(2**x)


# 2/9 feladat (Páratlan)

# for x in range(1,101,2): print(x)


# 2/10 feladat( Páratlan2) 

# for x in range(99,0,-2): print(x)


# 2/11 feladat (Számtanisor)

# for x in range (10,10+7*51,7): print(x)


# 2/12 feladat (Számtanisor2)

# n=int(input('Kérlek add meg egy számtani sorozat első tagját!  '))
# d=int(input('Add meg a differenciálját!  '))
# print(n, end=' ')
# for x in range(19):
#     print(n+d, end=' ')
#     n=n+d


# 2/13 feladat (Számtanisor3)

# print('Add meg egy számtani sorozat két szomszédos tagját!')
# szam1=int(input('Első szám:  '))
# szam2=int(input('Második szám:  '))
# d=szam2-szam1
# for _ in range(0,22):
#     print(f'{szam1-d*10}')
#     szam1=szam1+d


# 2/14 feladat (Hőmérséklet_átváltás)

# for c in range(-30, 31, 1):
#     print(f'{c}°C = {1.8*c+32:.1f}°F')


# 2/15 feladat (Kétjegyű3)

# for x in range(10,100):
#     if x % 3 == 0: print(x)


# 2/16 feladat (Osztók)

# szam=int(input('Adj meg egy számot!  '))
# x=1
# while x<=szam:
#     if szam % x ==0:
#         print(x)
#     x+=1


# 2/17 feladat (Prím_teszt)

# szoveg='Adj meg egy számot!  '
# szam=int(input(szoveg))
# if szam < 1: print('Csak pozitív egész szám lehet prím szám.')
# else:
#     y=0
#     for x in range(2,szam):
#         if szam % x == 0:
#             print(x)
#             y+=1
#     if y == 0: print('A szám prím')
#     else: print('Ezek a szám osztói.')


# 2/18 feladat (Inko)

# a=int(input('Add meg az első számot!  '))
# b=int(input('Add meg a másiodik számot!  '))
# c=None
# if a > 0 and b > 0 and a >= b:
#     for _ in range(a):
#         c = a % b
#         if c==0: break
#         a = b % c
#         if a==0: break
#         b = c % a
#         if b==0: break
#     if a==0: print(f'A legnagyobb közös osztó: {c}')
#     if b==0: print(f'A legnagyobb közös osztó: {a}')
#     if c==0: print(f'A legnegyobb közös osztó: {b}')
# if a > 0 and b > 0 and b > a:
#     for _ in range(b):
#         c = b % a
#         if c==0: break
#         b = a % c
#         if b==0: break
#         a = c % b
#         if a==0: break
#     if a==0: print(f'A legnagyobb közös osztó: {b}')
#     if b==0: print(f'A legnagyobb közös osztó: {c}')
#     if c==0: print(f'A legnagyobb közös osztó: {a}')


# 2/19 feladat (Szim3jegyű)

# for x in range(100, 1000):
#     x=str(x)
#     if x[0]==x[2]: print(x)


# 2/20 feladat (Fibonacci)

# a=0
# b=1
# c=1
# print(b,c,sep="\n")
# for x in range(0,3):
#     a=b+c
#     b=a+c
#     c=a+b
#     print(a, b, c, sep="\n")


# 2/21 feladat (Armstrong)

# for x in range(100,1000):
#     sz=x//100
#     t=(x-x//100*100)//10
#     e=x-x//10*10
#     if sz**3+t**3+e**3==x: print(x)


# 2/22 feladat (Faktor)

# n=1
# szam=int(input('Adj meg egy 0-nál nagyobb egész számot és kiszámolom a faktoriálisát!  '))
# for x in range(1,szam+1):
#     n=n*x
# print(f'A {szam} faktoriálisa: {n}')


# 2/23 feladat (6dobás)

# from random import randint
# x=0
# for _ in range(100):
#     dobas=randint(1,6)
#     if dobas==6: x+=1
# print(f'A száz dobásból {x} dobás volt 6-os')


# 2/24 feladat (Dobásösszeg12)

# from random import randint

# x=0
# for _ in range(20):
#     kocka1=randint(1,6)
#     kocka2=randint(1,6)
#     if kocka1+kocka2==12: x+=1
# print(f'{x} dobás összege volt 12.')


# 2/25 feladat (Sorösszeg)

# y=0
# for x in range(101):
#     y=y+x
# print(f'Az első 100 szám összege: {y}')


# 2/26 feladat (Dobásösszeg)

# from random import randint

# x=0
# for _ in range(100):
#     dobas=randint(1,6)
#     x=x+dobas
# print(f'A 100 dobás összege: {x}')


# 2/27 feladat (Szöveg_fordítva)

# szoveg=input('Írj be egy szöveget, kiírom fordítva!  ')
# for x in range(len(szoveg),0,-1):
#     print(szoveg[x-1], end="")


# 2/28 feladat (Név_átlósan)

# for x in range(0,10): print(x*'    '+'Bali Gábor')


# 2/29 feladat (Faktoriális)

# print('Az első tíz szám faktoriálisa')
# for x in range(0,10):
#     z=1
#     for y in range(1,x+1):
#         z=z*y
#     print(z)


# 2/30 feladat (prímek)

# for x in range(2,501):
#     z=0
#     for y in range(2,x): 
#         if x%y==0:
#             z+=1
#     if z==0: print(x)


# 2/31 feladat (Számok)

# sor=1
# while sor<=9:
#     oszlop=1
#     while oszlop<=sor:
#         print(f'{sor} ', end='')
#         oszlop+=1
#     print('') 
#     sor+=1


# 2/31/B feladat

# sor=1
# while sor<=9:
#     oszlop=1
#     while oszlop<=9:
#         if oszlop<sor: print('  ', end='')
#         if oszlop>=sor: print(f'{10-sor} ',end='')
#         oszlop+=1
#     print('')
#     sor+=1


# 2/32 feladat (Vakáció)

# szoveg='Vakáció'
# sor=0
# seged=0
# while sor<=len(szoveg)-1:
#     oszlop=1
#     seged=sor
#     while oszlop<=len(szoveg)-sor:
#         print(f'{szoveg[seged]} ',end='')
#         oszlop+=1
#         seged+=1
#     print('  ')
#     sor+=1


# 2/32/B feladat

# szoveg='V a k á c i ó '
# for x in range(len(szoveg),-1,-2): print(x*' '+szoveg[x:len(szoveg)])


# 2/33 feladat (Szorzótábla)

# sor=1
# while sor<=10:
#     oszlop=1
#     while oszlop<=10:
#         print(f'{oszlop*sor}   ',end='')
#         oszlop+=1
#     print(' ')
#     sor+=1


# 2/34 feladat (Pszeudoalgoritmus)

# for i in range(2, -1, -1):
#     for j in range(0, 3, 1):
#         if i==j:
#             print('1',end='')
#         else:
#             print('0',end='')
#     print('')


# 2/35 feladat ()
# Nem lehet végrehajtani.










