'''
 Karl Eerik Kotter
 31.01.2022
 Ülesanne 02
'''

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



#kuues
#kiirus
v = kiirus = 29.9
#aeg minututes
t = aeg = 0.4
s=v * t
print("nad jõudsid 24 minutiga",s,"km kaugusele")

