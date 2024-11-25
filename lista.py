# 3/1 feladat

# nevek=['Anna','Flóra','Ádám','Mónika','Gábor']
# print(nevek)
# magassag=[]
# for x in range(0,len(nevek)):
#     magassag.append(int(input(f'Add meg {nevek[x]} magasságát cm-ben.  ')))
# osszeg=sum(magassag)
# print(f'Az átlag magasság: {osszeg/len(magassag)} cm')
# csere=None
# for x in range(0,len(nevek)):
#     for y in range(1,len(magassag)):
#         if nevek[x] < nevek[y]:
#             csere=nevek[x]
#             nevek[x]=nevek[y]
#             nevek[y]=csere
#             csere=magassag[x]
#             magassag[x]=magassag[y]
#             magassag[y]=csere
# print(nevek)
# print(magassag)
# print(sorted(nevek))
# legmagasabb=max(magassag)
# legm_index=magassag.index(legmagasabb)
# print(f'A legmagasabb meber: {nevek[legm_index]} {legmagasabb} cm.')


# 3/2 feladat

# from random import randint

# szamok:int=[]
# csere=None
# for _ in range(0,20):
#     szamok.append(randint(50,150))
# for x in range(0,len(szamok)):
#     for y in range(x+1,len(szamok)):
#         if szamok[x]<szamok[y]:
#             csere=szamok[x]
#             szamok[x]=szamok[y]
#             szamok[y]=csere
# print(szamok)
# print(sorted(szamok))
# osszeg=0
# for x in range(len(szamok)):
#     osszeg=osszeg+szamok[x]
# print(f'A számok összege: {osszeg}')
# print(f'A számok átlaga: {osszeg/len(szamok)}')
# darab=0
# for x in range(len(szamok)):
#     if szamok[x] % 10 == 0:
#         darab+=1
# print(f'A 0-ra végződő számok szám: {darab} db')


# 3/3 feladat

# from random import randint

# szamok=[]
# x=0
# while len(szamok)<20:
#     uj_szam=randint(10,99)
#     if uj_szam>=x:
#         szamok.append(uj_szam)
#         x=uj_szam
# print(szamok)


# 3/4 feladat

# nevek=[]
# for _ in range(10):
#     nev=input('Adj meg egy nevet!  ')
#     if nev == '': break
#     nevek.append(nev)
# print(sorted(nevek))


# 3/5 feladat

# from random import randint

# paratlan=[]
# while len(paratlan)<50:
#     szam=randint(10,99)
#     if szam % 2 == 1:
#         paratlan.append(szam)
# print(paratlan)
# if 13 in paratlan: print('Szerepel benne 13-as szám.')
# else: print('Nem szerepel benne 13-as szám.')


# 3/6 feladat

# from random import randint

# szamok=[]
# while len(szamok)<50:
#     x=randint(10,99)
#     if x not in szamok:
#         szamok.append(x)
# print(szamok)


# 3/7 feladat

# from random import randint

# tipp=[]
# lotto=[]
# while len(tipp)<5:
#     szam=int(input(f'Add meg a(z) {len(tipp)+1}. tippedet!   '))
#     if szam<1 or szam>90: print('Csak 1 és 90 közötti szám adható meg!')
#     elif szam in tipp: print('Nem adható meg ugyanaz a szám!')
#     else: tipp.append(szam)
# while len(lotto)<5:
#     x=randint(1,90)
#     if x not in lotto:
#         lotto.append(x)
# print(f'A tippjeid:         {sorted(tipp)}')
# print(f'A heti nyerőszámok: {sorted(lotto)}')
# seged=0
# for x in lotto:
#     for y in tipp:
#         if y==x:
#             seged+=1
# if seged>0: print(f'{seged} találatod van.')
# else: print('Nincs találatod.')


# 3/8 feladat

# napi_adat=[]
# for x in range(12):
#     szam=int(input(f'Kérlek add meg a(z) {x+1}. napi átutalások számát:  '))
#     napi_adat.append(szam)
# print(f'Az átutalások napi átlaga: {round(sum(napi_adat)/len(napi_adat), 2)}')
# print('Az alábbi napokon volt átlag feletti az utalások száma:')
# for x in range(len(napi_adat)):
#     if napi_adat[x] > sum(napi_adat)/len(napi_adat):
#         print(f'{x+1}. napon {napi_adat[x]} db.')


#3/9 feladat

# sebesseg=[]
# rendszam=[]
# auto=0
# seb_adat=0
# while len(rendszam) <= 4:
#     auto=input(f'Kérem adja meg a(z) {len(rendszam)+1}. gépjármű rendszámát:  ')
#     if auto == '': break
#     rendszam.append(auto)
#     seb_adat=int(input('Kérem adja meg a gépjármű sebességét:  '))
#     sebesseg.append(seb_adat)
# for x in range(len(sebesseg)):
#     if sebesseg[x] > 90: print(f'{rendszam[x]} {sebesseg[x]} km/h ')
# if max(sebesseg) <= 90: print('Nem volt gyorshajtó.')


# 3/10 feladat

# from random import randint

# nev=['Laci','Peti','Jani','Józsi','Lajos']
# ido=[]
# for x in range(len(nev)):
#     ido.append(randint(0,9))
# print(f'A diákok átlagosan: {sum(ido)/len(ido)} órát interneteznek.')
# for x in range(len(ido)):
#     if ido[x] > 2:
#         print(f'{nev[x]} 2 óránál többet internetezik.')
# if 0 in ido:
#     print('Van olyan gyerek aki nem internetezik:')
# for x in range(len(ido)):
#     if ido[x] == 0: print(f'{nev[x]}')


# 3/11 feladat

# szamok=[]
# paros=0
# paratlan=0
# for x in range(0,40):
#     szamok.append(x*x%6)
#     if szamok[x]%2==0 and szamok[x]>0: paros+=1
#     if szamok[x]%2!=0 and szamok[x]>0: paratlan+=1
# print(szamok)
# if paros>paratlan: print('A páros szám a több.')
# elif paros<paratlan: print('A páratlan szám a több.')
# else: print('Ugynannyi a páros mint a páratlan szám. ')


# 3/12 feladat

# cella=[]
# for x in range(100): cella.append(0)
# for x in range(1,101):
#     for y in range(0,100, x):
#         cella[y] = not cella [y]
# for x in range(len(cella)):
#     if cella[x]==1: print(x)