from prettytable import PrettyTable

# creating an Object from the PrettyTable Class
table = PrettyTable()

# accessing methods
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])

# accessing attributes
table.align = "l"

print(table)

