import random


class CreateChar:
	
	def init_character(self):
		# Get character name from user
		self.name()
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
		return self.name, self.domain, self.hitpoints, self.strength, self.stamina


	def name(self):
		self.name = input("What is your name?\n>>> ")
		print("Nice to meet you {self.char_name}")
		return self.name
	
	
	def hitpoints(self, domain):
		self.domain = domain
		
		if self.domain == 'Rogue':
			self.hitpoints = random.randrange(5, 20)
			return self.hitpoints
		elif self.domain == 'Warrior':
			self.hitpoints = random.randrange(5, 18)
			return self.hitpoints
		elif self.domain == 'Fighter':
			self.hitpoints = random.randrange(5, 16)
			return self.hitpoints
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
			return self.stamina
		if self.domain == "Warrior":
			self.stamina = 90
			return self.stamina
		if self.domain == "Fighter":
			self.stamina = 100
			return self.stamina
		else:
			print("Error in player class, char_strength func")
			exit(0)


	def death(self, player_character):
		print(f"You have died, your beloved character {self.name} has met their ultimate fate...")
		print("Kiss {} goodbye... FOREVER!")
		del player_character
		print("Git gud noob, try again... if you are brave enough!")
		exit(0)