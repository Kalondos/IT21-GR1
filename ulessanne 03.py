'''
Karl Eerik Kotter
Ulesanne 03
01.02.2022
'''




#palindroom
palindroom = input("sisesta palindroom:")
print(palindroom == palindroom[::-1])

#tundide ajad

#Kasutaja sisestab tundide alguse ja lõpu
aeg1 = input("tundide algus: ")
aeg2 = input("tundide lõpp: ")
hh1, mm1 = aeg1.split(":")
hh2, mm2 = aeg2.split(":")
vastus = (int(hh2)*60+int(mm2)) - (int(hh1)*60+int(mm1))
h = vastus//60
m =vastus%60
print(f"Õpilase päeva pikkus on {hh}:{m}min")
#email
#programm küsib kasutajalt emaili kontot

email = input("Palun sisestage oma email: ")
#kontrollib @
print('@' in email)








#vandumine
#kasutaja sisestab sõna "kurat"
tekst = input('Palun ära kirjuta "kurat": ')
#programm repleicib sõna kurat tärnidega
tekst2 = tekst.replace('kurat', '*****')
#tekst väjastatakse
print(tekst2)



#korralik nimi
kasutajanimi = int(input("Sisestage oma nimi: "))
kasutajanimi = kasutajanimi.strip().capitalize()
print(kasutajanimi)