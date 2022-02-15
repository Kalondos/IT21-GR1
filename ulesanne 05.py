'''
Карл Эерик Kвартира
ULESANNE 05
10.02.2022
'''


'''
Tärnid
Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm.
Näiteks:
******************
*******************
********************************
*****************************************
****************************************************
************
'''
import plotly.express as px
import numpy
 
# creating random data through randomint
# function of numpy.random
np.random.seed(42)
   
random_x= np.random.randint(1, 101, 100)
random_y= np.random.randint(1, 101, 100)
 
fig = px.bar(random_x, y = random_y)
fig.show()

















'''
Vanused
Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine
'''


import random
vanused = []
for i in range(5):
    vanused.append(random.randint(1,99))
print(f"suurim arv: {max(vanused)}\nväiksem arv: {min(vanused)}\nkogusumma{sum(vanused)}\nkeskmine arv: {sum(vanused)/len(vanused)}")







'''
Duplikaadid
Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
opilased = [‘Juhan’,’Kati’,’Mario’,’Mario’,’Mati’,’Mati’]
Loo kood, mis ei väljasta kordusi.
'''
opilased = ['Junn','Karti','Miirold','Miirold','Märt','Märt']
puhas = []

for i in range(len(opilased)):
    if opilased[i] not in puhas: 
        puhas.append(opilased[i])

for i in range(len(puhas)):
    print(puhas[i],end=", ")







'''
Õpilased
Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
opilased = [‘Juhan’,’Kati’,’Maarja’,’Mario’,’Mati’]
'''
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
print("Vali nr, mida soovid muuta: ")
for i in range(len(opilased)):
    print(f"{i+1}. {opilased[i]}")
valik = int(input("Sisesta number: "))
del opilased[valik-1]
uus_nimi = input("sisenda omale nimi sisse: ")
opilased.insert(valik-1,uus_nimi)
print("suure noku energia")
print(opilased)










'''
Nimede lisamine loendisse
Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.
'''
#küsib kasutajalt viis nime
nimed = []
for i in range(5):
    nimi = input("Sisestage viis nime: ")
    nimed.append(nimi)
#tähestikulises järjekorras
nimed.sort()
#väljastab nimed
print(nimed)


    
    
