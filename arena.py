import random



def arena(player, enemy):
	player = player
	enemy = enemy
	p_hp = player.hitpoints
	e_hp = enemy.hitpoints
	p_max_hit = int(player.strength)
	e_max_hit = int(enemy.strength)
	
	print(f"You are in the arena!\nYou: {player.name}\t|\tEnemy: {enemy.race}")
	
	while True:
		attacker = random.randrange(1,3)
		p_str = random.randrange(1, p_max_hit)
		e_str = random.randrange(1, e_max_hit)
		
		if attacker == 1: # attacker 1 is the player
			e_hp = e_hp - p_str
			print(f"{player.name} hit {enemy.race} for {p_str}!\nThat leaves {enemy.race} with {e_hp} hitpoints!")
			pass
		elif attacker == 2: # attacker 2 is the enemy
			p_hp = p_hp - e_str
			print(f"{enemy.race} hit {player.name} for {e_str}!\nThat leaves {player.name} with {p_hp} hitpoints!")
			pass
		else:
			pass
		# deletes attacker num
		del attacker, p_str, e_str
		
		# Checks for death
		if p_hp <= 0 or e_hp <= 0:
			if p_hp <= 0:
				player.death(player)
			elif e_hp <= 0:
				print("You have slain the beast! You win!!!")
				exit(0)
			else:
				print("Error inside arena.py | while loop, 2nd if statement checking death")
				exit(0)
