################################################
# Karl Eerik Kodar
# Termomeeter
# UL 5
# 3/10/2022
################################################


import random


#teeb menüü
def menu():
    print ("[1] Termomeeter")
    print ("[2] Viimane mööt")
    print ("[0] Lahku")
    print ("NB! Programm nullib automaatselt kraadi algmöödu")

menu()
valik = int(input("sisesta valik: "))
#programm lõppeb kui kirjutada 0
while valik != 0:
    if valik == 1:
        termomeeter = list(range(-50, 50 + 1))
         # miinimum ja maksimum
        miinimum = min(termomeeter)
        maksimum = max(termomeeter)
        # väljastab miinimumi ja maksimumi
        print('Skaala miinimum:', miinimum, 'kraadi.\nSkaala maksimum', maksimum, 'kraadi.')

        # Valib randomly ühe numbri termomeetrist

        suvaline = [random.choice(termomeeter)]
        suvaline2 = suvaline
        suvaline[0]

        # väljastab kogu jama
        print("Praegult on", suvaline, "kraadi.")

    #teine valik mähib oma juttu, ez finess
    elif valik == 2:
        print("-----------------------------------\nkerige ülesse, et näha viimast möötu ;)\n-----------------------------------")
    #annab veateate kui valiti vale nr
    else:
        print("-----------------------------------\n    EBAÕNNESTUS!\nValisite vale numbri\n-----------------------------------")
    
    #Menüü loop, kestab kuniks pole suletud 
    print()
    menu()
    valik = int(input("sisesta valik: "))