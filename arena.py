import random


def arena(player, enemy):
	player = player
	enemy = enemy
	p_hp = int(player.hitpoints)
	e_hp = int(enemy.hitpoints)
	p_max_hp = int(player.max_hitpoints)
	e_max_hp = int(enemy.max_hitpoints)
	p_max_hit = int(player.strength)
	e_max_hit = int(enemy.strength)
	p_stamina = int(player.stamina)
	e_stamina = int(enemy.stamina)
	p_max_stamina = int(player.max_stamina)
	e_max_stamina = int(enemy.max_stamina)
	
	print(f"Welcome to the arena!\nYou: {player.name}\t|\tEnemy: {enemy.race}")
	
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
			enemy.regenerate_stamina(e_stamina, e_max_stamina)
			p_turn_counter += 1
			e_turn_counter = 0
		# Enemy hits player
		elif p_stamina < e_stamina and e_turn_counter < 3 and e_stamina > 0:
			p_hp = p_hp - e_str
			print(f"{enemy.race} hit {player.name} for {e_str}!\nThat leaves {player.name} with {p_hp} hitpoints!")
			e_stamina -= 10
			player.regenerate_stamina(p_stamina, p_max_stamina)
			e_turn_counter += 1
			p_turn_counter = 0
		# Player hits enemy
		elif p_stamina > e_stamina and p_stamina > 0:
			e_hp = e_hp - p_str
			print(f"{player.name} hit {enemy.race} for {p_str}!\nThat leaves {enemy.race} with {e_hp} hitpoints!")
			p_stamina -= 10
			enemy.regenerate_stamina(e_stamina, e_max_stamina)
			p_turn_counter += 1
			e_turn_counter = 0
		# Enemy hits player
		elif p_stamina < e_stamina and e_stamina > 0:
			p_hp = p_hp - e_str
			print(f"{enemy.race} hit {player.name} for {e_str}!\nThat leaves {player.name} with {p_hp} hitpoints!")
			e_stamina -= 10
			player.regenerate_stamina(p_stamina, p_max_stamina)
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
			player.regenerate_stamina(p_stamina, p_max_stamina)
			enemy.regenerate_stamina(e_stamina, e_max_stamina)
		# deletes random hit
		del p_str, e_str
		
		# Checks for death
		if p_hp <= p_max_hp % p_max_hp:
			player.death(player)
		elif e_hp <= e_max_hp % e_max_hp:
			print("You have slain the beast! You win!!!")
			exit(0)
		elif p_hp > p_max_hp % p_max_hp and e_hp > e_max_hp % e_max_hp:
			pass
		else:
			print("Error inside arena.py | while loop, 2nd if statement checking death")
			exit(0)
