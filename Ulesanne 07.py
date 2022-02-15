'''
Карл Эерик Kвартира
ULESANNE 07
15.02.2022
'''
import math

#kuup

def kuup(a):
    v = a ** 3
    return v

def kera(r):
    v = round(4/3*math.pi*r**3,2)
    return v

def koonus(r,h):
    v = round(1/3*math.pi*r**2*h,2)
    return v
def silinder(r,h):
    v = round(math.pi*r**2*h,2)
    return v

print("---------------------Leiame su ema kujundi------------------")
print("Vali kujund:\n1 Kuup\n2 Kera\n3 Koonus\n4 Silinder\n5 Lahku")
valik = int(input("Vali kujundi nr: "))

if valik == 1:
    print("**********************************************\nValisite kuubi, lollakas selline")
    a = int(input("sisesta kuubi külje pikkus a="))
    print(kuup(a))
    
if valik == 2:
    print("**********************************************\nValisite kera, lollakas selline")
    r = int(input("sisesta Kera mööt r="))
    print(kera(r))
    
if valik == 3:
    print("**********************************************\nValisite koonuse, lollakas selline")
    r = int(input("sisesta koonuse Sp: "))
    h = int(input("sisesta koonuse kõrgus: "))
    print(koonus(r,h))
    
if valik == 4:
    print("**********************************************\nValisite silindri, lollakas selline")
    r = int(input("sisesta silindri Sp="))
    h = int(input("sisesta silinder kõrgus: "))
    print(silinder(r,h))
    
if valik == 5:
    print("Soovisite lahkuda")
    r













'''
Koosta funktsioon, mille väljakutsumisel tevitab kasutajat tema enda nimega
tervita('Mario')    
'''

'''


#teen funtksiooni atribuutidega

def tervita(nimi, keel="de"):
    if keel=="et":#eesti keel
        print(f"tere {nimi}")
    elif keel=="en":#angliskii keel
        print(f"Hello {nimi}")
    else:#germany keel
        print(f"Ciao {nimi}")
    

n = input("Sisestage oma ema nimi: ")
k = input("Valige keel et/en/de: ")
#funktsiooni väljakutsumine
tervita(n,k)
'''