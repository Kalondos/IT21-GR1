'''
Карл Эерик Kвартира
ULESANNE 06
15.02.2022
'''





'''
Sellel aadressil asub nimekiri populaarsematest poliitikutest Facebookis: https://metshein.com/python/s6pru_l6ustaraamatus.txt
Sinu ülesanne on koostada programm, mis kuvab pooliitikud inimsilmale sõbralikus vaates.
'''
re, kesk = 0, 0
erakonnad = []
with open('s6pru_l6ustaraamatus.txt','r') as raamat:
    for rida in raamat:
        enimi, pnimi,er, likes = rida.split(" ")
        print(f"{enimi:11} {pnimi:11} {er:4} {likes:5}",end="")
        if er=="RE":
            re+=1
        elif er=="KE":
            kesk+=1
print(erakonnad)
print("\n************************************")
print(f"Reformikad: {RE}\nKeskmisi: {kesk}")
print(f"Erakondi kokku: {len(erakonnad)}")   
'''
Täienda eelmist programmi nii, et kuvataks kui palju on nimekirjas kodanikke Reformierakonnast ja kui palju Keskerakonnast
'''