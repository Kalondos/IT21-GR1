# Karl Eerik Kotter
# Ul 4
# 28/04/22



extends Node


func _ready():
	#mängijad
	var players = ["Feake","Bradwell","Dreger","Bloggett","Lambole","Daish","Lippiett","Blackie","Stollenbeck","Houseago","Dugall","Sprowson","Kitley","Mcenamin","Allchin","Doghartie","Brierly","Pirrone","Fairnie","Seal","Scoffins","Galer","Matevosian","DeBlase","Cubbin","Izzett","Ebi","Clohisey","Prater","Probart","Samwaye","Concannon","MacLure","Eliet","Kundt","Reyes"]
	#väljastab mängijate koguarvu
	print("Players: ",len(players),"\n")
	#esimene mängija massiivist
	print("First player of the array: ",(players[0]))
	# eemaldab nime 
	players.erase("Reyes")
	#lisan enda nime massiivi
	players.append("Kotter")
	#kõige pikem nimi massiivist
	print("\nLongest name: ",players.max(),"\n")
	#kuvab kõik mängijad
	print("All players in the list: \n")
	for player in players:
		print(player)
