'''
 Karl Eerik Kotter
 31.01.2022
 Ülesanne 02
'''
print("----------------------------------------------")
import math
#kasutaja sisestab kütuse kulu
kytus = int(input("Sisestage tangitud kütuse liitrid: "))
#ksautaja sisesatb läbitud km
km = int(input("Sisestage läbitud kilomeetrid: "))

keskmine = kytus/km*100
print(keskmine)
print("----------------------------------------------")


#3 täisarvulist muutujat
a = 1
b = 2
c = 3
#valem
p=a+b+c
#väljastan vastuse
print('Kolmnurga ümbermõõt on:',p)



print("----------------------------------------------")

#Toote hind
hind = 36.75
#allahindlus
ah = 0.4
#summa ümardatuna
summa = round(hind-(hind*ah))*3
#v2ljastab summa 
print("Kolme toote hind:",summa,"€")




print("----------------------------------------------")
#pitsa hind
hind = 12.90
#jootraha
jr = 0.1
#jootraha summa
x = hind*jr
#väljastab jootraha summa
print("Nad peavad maksma",x,"€ jootraha")




print("----------------------------------------------")
#kiirus
v = kiirus = 29.9
#aeg minututes
t = aeg = 0.4
s=v * t
print("Nad jõudsid 24 minutiga",s,"km kaugusele")





print("----------------------------------------------")
#külg a
a = 16
#külg b
b = 9
#valem, et saada hüpotenuusi
x = math.sqrt(a**2+b**2)
#väjastan hüpotenuusi
print("Kolmnurga hüpotenuus on ",x,"cm2")






print("----------------------------------------------")
#aja sisestamine minutis
aeg = int(input("Sisestage aeg minutites: "))
#teisendab minutid tundideks
tund = aeg//60
#
minut = aeg%60
print(aeg, "minutit on", tund,"h", minut,"min")




print("----------------------------------------------")
#kasutaja sisendab täisarvu kümnendsüsteemis
arv = int(input("Sisestage kümnendsüsteemis täisarv: "))
#väljastab bineaarina
print(bin(arv))
#väljastab hexina
print(hex(arv))
print("----------------------------------------------")


 
