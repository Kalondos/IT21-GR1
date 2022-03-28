print("\n------------ Vägimees Leiger ------------\n")

#https://python.hotexamples.com/examples/gameStats/GameStats/-/python-gamestats-class-examples.html

def menu():
    print("[1] Alustage mänguga.")
    print("[2] Legend.")
    print("[3] Lahku mängust.")
    
menu()
valik = int(input("Sisestage valik: "))

while valik != 3:
    if valik == 1:
        #statid
        elud = 0 #max 100
        xp = 0 
        level = 0 #10 xpd 1 level
        jõud = 0 #max 10
        armor = 0 #max 50
        skoor = 0 #uueneb vastavalt

        print("\n(Pühapäev, kell 09.18)\nArkasite just suure müra peale.\n")
        
        def valik_1():
            print("[1] Tõusete püsti ja lähete asja uurima.\n")
            print("[2] Teil on suva sellest mürast ja magate edasi.")
        valik_1()
        
        if valik == 1:
            pass
        elif valik == 2:
            print("magate edasi")
        
        
        
        
        
        
        
        
        
        
        
    elif valik == 2:
        print("Selsamal ajal, kui Suur Tõll Saaremaal tähtsaid töösid tegi, elas Hiiumaal Tõlli vennapoeg Leiger. Seegi oli niisamasugune tugev mees nagu Suur Tõll, ehk küll viimane jõu poolest temast, üle käis. Leiger ja Suur Tõll armastasivad mõlemad vihtlemist. Suur Tõll käskinud Leigri sauna ehitada,tal enesel polla ehituseks aega. Leiger hakanudki tööle. Vedanud kümne sülla pikkused palgid metsast välja.Neist ehitanud siis vihtlemisesauna. Ahi saanud nii suur nagu saunamehe saun. Kerisekivideks üksi vedanud Leiger seitse sülda ümmargusi kiva kokku. Kui saun valmis saanud, tulnud Suur Tõll Hiiumaale sagedasti vihtlema. Leiger kütnud ahju tublisti soojaks, võtnud siis kummagi õla peale vaadi vett ja viinud leile viskamiseks sauna. Peale selle tapnud Leiger iga korra, kui Suur Tõll sauna tulnud, kaks härga ja keetnud need ära. Saunast ära tulles kutsunud Leiger Suure Tõlli ikka enese juure sööma. Kumbki söönud terve härja ja teo leiva ära. Olnud kõht täis, siis läinud Suur Tõll Saaremaale magama, Leiger aga heitnud tihti sauna leiba luusse laskema. Kuid, siis kui Leiger magas tuli vanapagan kes viis Leigri naise minema ning nii pidigi Leiger asuma pikale retkele.")    
    else:
        print("Sisestasite vale numbri")
    print()
    menu()
    valik = int(input("Sisestage oma valik: "))
    
print("Tänud kasutamast meie naturaalset produkti")











