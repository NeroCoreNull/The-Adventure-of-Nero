from player import CreateChar
from enemy import CreateEnemy
import arena
# import enemy
# import arena


def main():
	player = CreateChar()
	player.init_character()
	
	enemy = CreateEnemy()
	enemy.init_enemy()
	
	print(f"\n    Here is your stats:\n\tName: {player.name}\n\tDomain: {player.domain}\n\tHitpoints: {player.hitpoints}\n\tStrength: {player.strength}\n\tStamina: {player.stamina}")
	print(f"\n    Your enemy:\n\tType: {enemy.race}\n\tHitpoints: {enemy.hitpoints}\n\tStrength: {enemy.strength}\n\tStamina: {enemy.stamina}")
	
	arena.arena(player, enemy)

if __name__ == "__main__":
	main()
