import random


class CreateChar:
    def name(self, char_name):
        self.char_name = char_name
        print(f"Pleased to meet you {char_name}")
        return self.char_name

    def rogue_class(self, char_name):
        print(f"Hello {char_name}, it's so good to see you")

        print("Let's generate you some free stats!")
        self.char_strength = random.randrange(1, 10)
        print(f"You rolled a {self.char_strength} for strength")
        self.char_hitpoints = random.randrange(5, 20)
        print(f"You rolled a {self.char_hitpoints} for your hitpoints")

        return self.char_strength, self.char_hitpoints

    def warrior_class(self, char_name):
        print(f"Hello {char_name}, it's so good to see you")

        print("Let's generate you some free stats!")
        char_strength = random.randrange(2, 12)
        self.char_strength = char_strength
        char_hitpoints = random.randrange(5, 18)
        self.char_hitpoints = char_hitpoints

        print(f"You rolled a {self.char_strength} for strength")
        print(f"You rolled a {self.char_hitpoints} for your hitpoints")

        return self.char_strength, self.char_hitpoints

    def fighter_class(self, char_name):
        self.char_name = char_name
        print(f"Hello {char_name}, it's so good to see you")

        print("Let's generate you some free stats!")
        self.char_strength = random.randrange(4, 14)
        print(f"You rolled a {self.char_strength} for strength")
        self.char_hitpoints = random.randrange(5, 16)
        print(f"You rolled a {self.char_hitpoints} for your hitpoints")

        return self.char_strength, self.char_hitpoints


def arena():
    pass


def main():
    player_character = CreateChar()

    char_name = input("What is your name? >>> ")
    player_character.name(char_name)

    temp_char_class = input(
        f"What do you want your class to be {player_character.char_name}? >>> "
    )
    if temp_char_class == "rogue":
        pass
    elif temp_char_class == "warrior":
        pass
    elif temp_char_class == "fighter":
        pass

    print(
        f"{player_character.char_name}, {player_character.char_age}, {player_character.char_strength}{player_character.char_hitpoints}"
    )


if __name__ == "__main__":
    main()
