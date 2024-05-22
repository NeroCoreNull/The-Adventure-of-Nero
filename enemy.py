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
		return self.race, self.hitpoints, self.max_hitpoints ,self.strength, self.stamina, self.max_stamina
		
		
	def hitpoints(self, race):
		self.race = race
		# no hitpoint change based on race yet
		self.hitpoints = random.randrange(1,10)
		self.max_hitpoints = self.hitpoints
		return self.hitpoints, self.max_hitpoints

	
	def strength(self, race):
		self.race = race
		# no strength change based on race yet
		self.strength = random.randrange(2,4)
		return self.strength
	
	
	def stamina(self, race):
		self.race = race
		# no stamina change based on race yet
		self.stamina = random.randrange(40, 80, 5)
		self.max_stamina = self.stamina
		return self.stamina, self.max_stamina
		
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
		
	def regenerate_stamina(self, stamina, max_stamina):
		self.stamina = stamina
		self.max_stamina = max_stamina
		if self.stamina >= self.max_stamina:
			return self.stamina, self.max_stamina
		elif self.stamina < self.max_stamina:
			self.stamina += 2.5
			if self.stamina >= self.max_stamina:
				self.stamina = self.max_stamina
			return self.stamina, self.max_stamina
		else:
			print("Error instide player.py | regenerate_stamina func")
			exit(0)