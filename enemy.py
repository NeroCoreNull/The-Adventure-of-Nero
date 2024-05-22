import random


class CreateEnemy:
	
	def init_enemy(self):
		# get race
		x = random.randrange(1,3)
		if x == 1:
			self.race = 'Goblin'
		elif x == 2:
			self.race = 'Cyclops'
		else:
			print("Error choosing race. Enemy.py - init_enemy")
			exit(0)
		
		self.hitpoints(self.race)
		self.strength(self.race)
		self.stamina(self.race)
		return self.race, self.hitpoints, self.strength, self.stamina
		
		
	def hitpoints(self, race):
		self.race = race
		# no hitpoint change based on race yet
		self.hitpoints = random.randrange(1,10)
		return self.hitpoints

	
	def strength(self, race):
		self.race = race
		# no strength change based on race yet
		self.strength = random.randrange(2,4)
		return self.strength
	
	
	def stamina(self, race):
		self.race = race
		# no stamina change based on race yet
		self.stamina = random.randrange(40, 80, 5)
		return self.stamina
		
	def regenerate_stamina(self, stamina):
		self.stamina = stamina
		max_stamina = self.stamina
		if self.stamina >= max_stamina:
			return self.stamina
		elif self.stamina < max_stamina:
			self.stamina += 2.5
			if self.stamina >= max_stamina:
				self.stamina = max_stamina
			return self.stamina
		else:
			print("Error instide player.py | regenerate_stamina func")
			exit(0)