# Karl eerik kotter
# 13.04.22
# Ul1
extends Node
func _ready():
	#nimi 
	var nimi = "goblin"
	print("nimi: ",nimi)
	
	#elud
	var health = 50
	print("elud: ",health)

	#nime pikkus
	print("nime pikkus: ",len(nimi))
	
	#m2ngija elude arv +2
	print("teil on nüüd elusid: ",health+2)
	
	#arvud 0-19 suvaliseslt
	print("suvaline arv: ",randi() % 20)
