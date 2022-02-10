
'''
Карл Эерик Kвартира
ULESANNE 04
03.02.2022
'''

'''
Ruutude ja kuupide tabel
Programm leiab ja väljastama ruudud ja kuubid arvudele 1..10.
Vorminda tabel tulpades.
Arv Ruut Kuup
1   1    1
2   4    8
3   9    27
4   16   64
jne
'''
for i in range(1,11):
    print(f"{i:5} {i**2:5} {i**3:5}")







'''
Pank
Kasutaja soovib panka panna raha teatud aastateks.
Panga intress on 5% summast. Leia kui palju ta summa iga aasta kasvab.
Vorminda tabel tulpades.
Näiteks: paneme panka 10000€ ja 5 aastaks
Aasta   Algsumma    Intress     Aasta lõpuks
1       10000.00    500.00      10500.00
2       10500.00    525.00      11025.00
3       11025.00    551.25      11576.25
4       11576.25    578.81      12155.06
5       12155.06    607.75      12762.82
Summa kokku: 12762.82€
Kasum: 2762.82€
'''
konto  = 0
raha = 10000
intress = 0.05
aastad = 5
konto += raha
print(f"{'asda':4} {'alksuMa':10} {'indersSs':10} {'astda lobugs':10}")
for i in range(aastad):
    kasum = konto*intress
    print(f"{i:4} {konto:10.2f},{kasum:10.2f},{konto+kasum:10.2f}")
    konto+=kasum
    











'''
arvamis,äng

loop = 1
korrad = 1
suv = random.randint(1,10)

while loop == 1:
    if korrad <= 3:
        arv = int(input("arva arv 1-10: "))
    else:
        veel = input("uuesti= jah/ei:")
        if veel == "jah":
            korrad = 0
        else:
            loop = 0
            
    korrad += 1
    if arv == suv
        print("arvasid ära")
                loop
            '''
                
            
    

print("---------------------------------------------------------------------")
'''
Pisike korrutustabel
Koosta programm, mis tekitab automaatselt viiega korrutustabeli.
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

for k in range(1,11):
    arv = 5
    v = k * arv
    print(f"{arv} x {k} = {v}")











print("---------------------------------------------------------------------")
'''
Paaris ja paaritu
Loo tsükkel, mis genereerib arvud 1-100 koos vastava tekstiga, kas arv on paaris või paaritu
'''
for i in range(1,11):
    if i%2==0:
        print(i, "paaris")
    else:
        print(i, "paaritu")





















print("---------------------------------------------------------------------")
'''
Loto
Koosta tsükli abil programm, mis kuvab 5 suvalist  ühekohalist numbrit. Näiteks 53542
'''
import random
print(random.randrange(0,99999))

print("---------------------------------------------------------------------")
'''
Tärnid
Loo tsükkel, mis väljastab 5×5 tärnid
Loo tsükkel, mis väljastab tärnidest kasvava kolmnurga
Loo tsükkel, mis väljastab tärnidest kahaneva kolmnurga
'''
k = 5
for i in range(1,6):
        print("¤    "* k)
        k += 1
for a in range(1,6):          
    for b in range(1,6):       
        print("¤    ", end='')
    print()
k = 5
for i in range(1,6):
        print("¤    "* k)
        k -= 1


    
    
    
    
    
    






print("---------------------------------------------------------------------")
'''
Jalgpalli meeskond
Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
'''
sugu = input("Sisestage oma sugu M/N: ")
if sugu == "M":
    vanus = int(input("Sisestage oma vanus: "))
    if vanus >= 16 and vanus <= 18:
        print("tim")
else :
    print("pähpäh")

print("---------------------------------------------------------------------")
#müüt
arv = int(input("Sisesta toote hind: "))
if arv <= 10:
    ah = 0.1
else :
    ah = 0.2   
#arvutab vastava allahindluse ära
hind = arv - (arv * ah)
print("Toote hind on", hind)


print("---------------------------------------------------------------------")
#jubel
sunnipaev = input("Sisesta oma sünnipäev dd.mm.yyyy: ")
d,m,y = sunnipaev.split(".")
aasta = 2022
vanus = aasta - int(y)
jaak = vanus % 5
if jaak == 0:
    print("jubel")
else:
    print("no jubel")
print("---------------------------------------------------------------------")
#Matemaatika
a1 = int(input("1. arv: "))
a2= int(input("2. arv: "))
#väljastab millist tehet ta soovib
tehe = input("Millist tehet te soovite :\n 1. Liitmine\n 2.Lahutamine\n 3.Korrutamine\n 4.Jagamine \n: " )
if tehe == "1":
    #liitmine
    tehe1 = (print(a1 ,"+", a2  ,"=",  a1 + a2))
elif tehe == "2":
    #lahutamine
    tehe1 = (print(a1 ,"-", a2 ,"=",  a1 - a2))
elif tehe == "3":
    #korrutamine
     tehe1 = (print(a1 ,"*", a2 ,"=",  a1 * a2))
elif tehe == "4":
    #jagamine
     tehe1 =(print(a1 ,"/", a2 ,"=",  a1 / a2))
print(tehe1)
print("---------------------------------------------------------------------")
#RUUT
A = int(input("1. külg: "))
B = int(input("2. Külg: "))
#kui a = b siis on tegemist ruuduga         
if A==B:
    print("Ruut")
    #kui a ei = b siis on tegemist ristkülikuga
else:
    print("Ristkülik")
    
    
    

