import random



def arena(player, enemy):
	player = player
	enemy = enemy
	p_hp = player.hitpoints
	e_hp = enemy.hitpoints
	p_max_hit = int(player.strength)
	e_max_hit = int(enemy.strength)
	p_stamina = player.stamina
	e_stamina = enemy.stamina
	
	print(f"You are in the arena!\nYou: {player.name}\t|\tEnemy: {enemy.race}")
	
	p_turn_counter = 0
	e_turn_counter = 0
	while True:
		p_str = random.randrange(1, p_max_hit)
		e_str = random.randrange(1, e_max_hit)
		
		# Player hits enemy
		if p_stamina > e_stamina and p_turn_counter < 3 and p_stamina > 0:
			e_hp = e_hp - p_str
			print(f"{player.name} hit {enemy.race} for {p_str}!\nThat leaves {enemy.race} with {e_hp} hitpoints!")
			p_stamina -= 10
			enemy.regenerate_stamina(e_stamina)
			p_turn_counter += 1
			e_turn_counter = 0
		# Enemy hits player
		elif p_stamina < e_stamina and e_turn_counter < 3 and e_stamina > 0:
			p_hp = p_hp - e_str
			print(f"{enemy.race} hit {player.name} for {e_str}!\nThat leaves {player.name} with {p_hp} hitpoints!")
			e_stamina -= 10
			player.regenerate_stamina(p_stamina)
			e_turn_counter += 1
			p_turn_counter = 0
		# Player hits enemy
		elif p_stamina > e_stamina and p_stamina > 0:
			e_hp = e_hp - p_str
			print(f"{player.name} hit {enemy.race} for {p_str}!\nThat leaves {enemy.race} with {e_hp} hitpoints!")
			p_stamina -= 10
			enemy.regenerate_stamina(e_stamina)
			p_turn_counter += 1
			e_turn_counter = 0
		# Enemy hits player
		elif p_stamina < e_stamina and e_stamina > 0:
			p_hp = p_hp - e_str
			print(f"{enemy.race} hit {player.name} for {e_str}!\nThat leaves {player.name} with {p_hp} hitpoints!")
			e_stamina -= 10
			player.regenerate_stamina(p_stamina)
			e_turn_counter += 1
			p_turn_counter = 0
		# Resets and loops
		else:
			e_hp = e_hp - p_str
			print(f"{player.name} hit {enemy.race} for {p_str}!\nThat leaves {enemy.race} with {e_hp} hitpoints!")
			p_hp = p_hp - e_str
			print(f"{enemy.race} hit {player.name} for {e_str}!\nThat leaves {player.name} with {p_hp} hitpoints!")
			p_turn_counter = 0
			e_turn_counter = 0
			player.regenerate_stamina(p_stamina)
			enemy.regenerate_stamina(e_stamina)
		# deletes random hit
		del p_str, e_str
		
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
