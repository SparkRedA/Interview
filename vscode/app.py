
print("Welcome to the Pokemon Trainer Quiz!")
print("Let's find out what kind of Pokemon trainer you are!\n")

# Question 1
pokemon = input("What is your favorite Pokemon type? ")

if pokemon.lower() == "fire":
    print("Awesome! Fire-type Pokemon are powerful!")
elif pokemon.lower() == "water":
    print("Nice! Water-type Pokemon are great in battle!")
elif pokemon.lower() == "grass":
    print("Cool! Grass-type Pokemon are strong and reliable!")
else:
    print("That's an interesting choice!")

# Question 2
starter = input("\nWho would you choose as your starter: Charmander, Squirtle, or Bulbasaur? ")

if starter.lower() == "charmander":
    print("Great choice! Charmander can become a powerful Charizard!")
elif starter.lower() == "squirtle":
    print("Good choice! Squirtle can become a powerful Blastoise!")
elif starter.lower() == "bulbasaur":
    print("Nice! Bulbasaur can become a powerful Venusaur!")
else:
    print("Interesting starter choice!")

# Question 3
legendary = input("\nIf you could catch one legendary Pokemon, which would it be? ")

if legendary.lower() == "mewtwo":
    print("Amazing! Mewtwo is one of the strongest legendary Pokemon!")
elif legendary.lower() == "rayquaza":
    print("Awesome! Rayquaza is an incredibly powerful Pokemon!")
elif legendary.lower() == "mew":
    print("Cool! Mew is a very rare and mysterious Pokemon!")
else:
    print("That's a cool legendary Pokemon choice!")

print("\nThanks for taking the Pokemon Trainer Quiz!")
print("Good luck on your Pokemon journey!")
