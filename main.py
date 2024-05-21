import random

class CreateChar:
    def name(self, char_name):
        self.char_name = char_name
        print(f"Pleased to meet you {char_name}")
        return char_name

    def rogue(self, char_name, char_age):
        self.char_name = char_name
        self.char_age = char_age
        print(f"Hello {char_name}, it's so good to see you")

        print("Let's generate you some free stats!")
        self.char_strength = random.randrange(1, 10)
        print(f"You rolled a {self.char_strength} for strength")
        self.char_hitpoints = random.randrange(5, 20)
        print(f"You rolled a {self.char_hitpoints} for your hitpoints")

        if self.char_age > 45:
            self.char_strength = self.char_strength - 3
            print("You are a tad old so you do get decreased strength")
            if self.char_strength <= 0:
                self.char_strength = 1

        return (self.char_strength, self.char_hitpoints)

    def warrior(self, char_name, char_age):
        self.char_name = char_name
        self.char_age = char_age
        print(f"Hello {char_name}, it's so good to see you")

        print("Let's generate you some free stats!")
        self.char_strength = random.randrange(2, 12, 2)
        print(f"You rolled a {self.char_strength} for strength")
        self.char_hitpoints = random.randrange(5, 18)
        print(f"You rolled a {self.char_hitpoints} for your hitpoints")

        if self.char_age > 45:
            self.char_strength = self.char_strength - 3
            print("You are a tad old so you do get decreased strength")
            if self.char_strength <= 0:
                self.char_strength = 1

        return (self.char_strength, self.char_hitpoints)

    def fighter(self, char_name, char_age):
        self.char_name = char_name
        self.char_age = char_age
        print(f"Hello {char_name}, it's so good to see you")

        print("Let's generate you some free stats!")
        self.char_strength = random.randrange(4, 14, 2)
        print(f"You rolled a {self.char_strength} for strength")
        self.char_hitpoints = random.randrange(5, 16)
        print(f"You rolled a {self.char_hitpoints} for your hitpoints")

        if self.char_age > 45:
            self.char_strength = self.char_strength - 3
            print("You are a tad old so you do get decreased strength")
            if self.char_strength <= 0:
                self.char_strength = 1

        return (self.char_strength, self.char_hitpoints)


def arena():
    pass


def main():
    player_character = CreateChar()
    char_name = input("What is your name? >>> ")
    player_character.name(char_name)
    char_age = input(f"Of what age are you, {player_character.char_name}? >>> ")

    char_class = input(
        f"What do you want your class to be {player_character.char_name}? >>> "
    )
    if "r" in char_class:
        player_character.rogue(char_name, char_age)
    elif "w" in char_class:
        player_character.rogue(char_name, char_age)
    elif "f" in char_class:
        player_character.rogue(char_name, char_age)
    else:
        pass

    print(
        f"{player_character.char_name}, {player_character.char_age}, {player_character.char_strength}, {player_character.char_hitpoints}"
    )


if __name__ == "__main__":
    main()
