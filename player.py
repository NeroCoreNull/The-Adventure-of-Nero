import random


class CreateChar:
# <-- INITIALIZATION -->
	def init_character(self):
		# Get character name from user
		self.name = input("What is your name?\n>>> ")
		print("Nice to meet you {self.char_name}")
		# Get character class
		temp_domain = ''
		while True:
			temp_domain = input("Make your choice:\nrogue  |  warrior  |  fighter\n>>> ")
			if temp_domain == "rogue":
				self.domain = "Rogue"
				break
			elif temp_domain == "warrior":
				self.domain = "Warrior"
				break
			elif temp_domain == "fighter":
				self.domain = "Fighter"
				break
			else:
				print(f"{temp_domain} is not a listed class. Try again:")
				temp_domain = ''
				pass
		# Get initial stats
		self.hitpoints(self.domain)
		self.strength(self.domain)
		self.stamina(self.domain)
		# return all values to main.py main func
		return self.name, self.domain, self.hitpoints, self.max_hitpoints,  self.strength, self.stamina, self.max_stamina

# <-- PLAYER STATS  -->
	def hitpoints(self, domain):
		self.domain = domain
		if self.domain == 'Rogue':
			self.hitpoints = random.randrange(5, 20)
			self.max_hitpoints = self.hitpoints
			return self.hitpoints, self.max_hitpoints
		elif self.domain == 'Warrior':
			self.hitpoints = random.randrange(5, 18)
			self.max_hitpoints = self.hitpoints
			return self.hitpoints, self.max_hitpoints
		elif self.domain == 'Fighter':
			self.hitpoints = random.randrange(5, 16)
			self.max_hitpoints = self.hitpoints
			return self.hitpoints, self.max_hitpoints
		else:
			print("Error in player class, char_health func")
			exit(0)


	def strength(self, domain):
		self.domain = domain
		if self.domain == "Rogue":
			self.strength = random.randrange(2, 10)
			return self.strength
		if self.domain == "Warrior":
			self.strength = random.randrange(2, 12)
			return self.strength
		if self.domain == "Fighter":
			self.strength = random.randrange(4, 14)
			return self.strength
		else:
			print("Error in player class, char_strength func")
			exit(0)
	
	def stamina(self, domain):
		self.domain = domain
		if self.domain == "Rogue":
			self.stamina = 110
			self.max_stamina = self.stamina
			return self.stamina, self.max_stamina
		if self.domain == "Warrior":
			self.stamina = 90
			self.max_stamina = self.stamina
			return self.stamina, self.max_stamina
		if self.domain == "Fighter":
			self.stamina = 100
			self.max_stamina = self.stamina
			return self.stamina, self.max_stamina
		else:
			print("Error in player class, char_strength func")
			exit(0)
	
# <-- REGENERATION FUNCTIONS -->
	def regenerate_hitpoints(self, hitpoints):
		self.hitpoints = hitpoints
		self.max_hitpoints = self.max_hitpoints
		if self.hitpoints >= self.max_hitpoints:
			return self.hitpoints
		elif self.hitpoints < self.max_hitpoints:
			if self.hitpoints <= 0:
				self.death(self.name)
			self.hitpoints = random.randrange(2,6)
			if self.hitpoints >= self.max_hitpoints:
				self.hitpoints = self.max_hitpoints
		return self.hitpoints
	
	def regenerate_stamina(self, stamina):
		self.stamina = stamina
		max_stamina = self.stamina
		if self.stamina >= max_stamina:
			return self.stamina
		elif self.stamina < max_stamina:
			self.stamina += 5
			if self.stamina >= max_stamina:
				self.stamina = max_stamina
			return self.stamina
		else:
			print("Error instide player.py | regenerate_stamina func")
			exit(0)


# <-- DEATH FUNCTIONS -->
	def death(self, player_character):
		print(f"You have died, your beloved character {self.name} has met their ultimate fate...")
		print("Kiss {} goodbye... FOREVER!")
		del player_character
		print("Git gud noob, try again... if you are brave enough!")
		exit(0)