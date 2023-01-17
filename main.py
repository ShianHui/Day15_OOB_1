from prettytable import PrettyTable

pokemon_table = PrettyTable()

pokemon_table.add_column("Pokemon", ["Pikachu", "Chamander", "Squirtle", ])
pokemon_table.add_column("Type", ["Electric", "Fire", "Water", ])
print(pokemon_table)
pokemon_table.align = "l"
print(pokemon_table)

