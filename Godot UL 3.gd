# karl eerik kotter
# 13.04.22
# ul3


extends Node
func _ready():
	
	var rng = RandomNumberGenerator.new()
	
	#Elud
	var enemyHealth = 100
	var enemyHealth_2 = 100
	#P1 ja P2 hitid
	var enemyPunch = round(rng.randf_range(8,15))
	var enemyPunch_2 = round(rng.randf_range(8,15))
	
	while enemyHealth > 0:
		
		enemyHealth -= enemyPunch_2
		enemyHealth_2 -= enemyPunch
		
		print("P1 Hit: ",enemyPunch, " | P1 Life: ",enemyHealth)
		print("P2 Hit: ",enemyPunch_2, " | P2 Life: ",enemyHealth_2)
		
		if enemyHealth <= 0:
			
			print("P2 Won")
			break
			
		else:
		
			if enemyHealth < 0:
				print("P1 Won")
				break
