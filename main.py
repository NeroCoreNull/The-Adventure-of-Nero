import random


class CreateChar:
	
	def name(self, char_name):
		self.char_name = char_name
		return self.char_name

	def rogue_class(self, char_name, char_class):
		self.char_name = char_name
		self.char_class = "Rogue"
		print(f"Hello {self.char_name}, it's so good to see you!\nYou picked a {self.char_class}...\n\tGreat choice!\n")
		
		print("Let's generate your initial stats!")
		self.char_strength = random.randrange(1, 10)
		print(f"You rolled a {self.char_strength} for strength")
		self.char_hitpoints = random.randrange(5, 20)
		print(f"You rolled a {self.char_hitpoints} for your hitpoints")
		self.char_stamina = 110
		print(f"Since you are a {char_class}, you get {self.char_stamina} stamina!")
		
		return self.char_class, self.char_strength, self.char_hitpoints, self.char_stamina

	def warrior_class(self, char_name, char_class):
		self.char_name = char_name
		self.char_class = "Warrior"
		print(f"Hello {self.char_name}, it's so good to see you!\nYou picked a {self.char_class}...\n\tGreat choice!\n")
		
		print("Let's generate your initial stats!")
		self.char_strength = random.randrange(2, 12)
		print(f"You rolled a {self.char_strength} for strength")
		self.char_hitpoints = random.randrange(5, 18)
		print(f"You rolled a {self.char_hitpoints} for your hitpoints")
		self.char_stamina = 90
		print(f"Since you are a {char_class}, you get {self.char_stamina} stamina!")
		
		return self.char_class, self.char_strength, self.char_hitpoints, self.char_stamina

	def fighter_class(self, char_name, char_class):
		self.char_name = char_name
		self.char_class = "Fighter"
		print(f"Hello {self.char_name}, it's so good to see you!\nYou picked a {self.char_class}...\n\tGreat choice!\n")
		
		print("Let's generate your initial stats!")
		self.char_strength = random.randrange(4, 14)
		print(f"You rolled a {self.char_strength} for strength")
		self.char_hitpoints = random.randrange(5, 16)
		print(f"You rolled a {self.char_hitpoints} for your hitpoints")
		self.char_stamina = 100
		print(f"Since you are a {char_class}, you get {self.char_stamina} stamina!")
		
		return self.char_class, self.char_strength, self.char_hitpoints, self.char_stamina


def arena():
	pass


def main():
	player_character = CreateChar()
	
	char_name = input("What is your name?\n>>> ")
	player_character.name(char_name)
	
	print(f"\nNice to meet you! What class would you like to play {player_character.char_name}?\n")
	temp_char_class = ''
	while True:
		temp_char_class = input("Make your choice:\nrogue  |  warrior  |  fighter\n>>> ")
		if temp_char_class == "rogue":
			player_character.rogue_class(char_name, temp_char_class)
			break
		elif temp_char_class == "warrior":
			player_character.warrior_class(char_name, temp_char_class)
			break
		elif temp_char_class == "fighter":
			player_character.fighter_class(char_name, temp_char_class)
			break
		else:
			print(f"{temp_char_class} is not a listed class. Try again:")
			temp_char_class = ''
			continue

	print(f"{player_character.char_name}, {player_character.char_class}, {player_character.char_strength}, {player_character.char_hitpoints}")


if __name__ == "__main__":
	main()
