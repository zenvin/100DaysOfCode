################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # will print 2

increase_enemies()
print(f"enemies outside function: {enemies}") # will print 1

# Local Scope (exist within functions)

# def drink_portion():
#     potion_strength = 2
#     print(potion_strength)

# drink_portion()
# print(potion_strength) # Error: potion strength is not defined. 

# Global Scope
# player_health = 10 #Global variable

# def game():
#     def drink_potion():
#         potion_strength = 2 #Local variable
#         print(player_health)
#     drink_potion()

# drink_potion() # Will Errror

# Applies to function and variables. 

# No Block Scope in Python

game_level = 3
enemies = ['zombies', 'skeleton', 'alien']

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy) # will print

#but if we embed the variable new_enemy, will not print

# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]

# print(new_enemy) # will print

# If the variable is created in a fucntion, it is in that function's scope.
# If the variable is made from a for loop, if loop, while loop, it is global.