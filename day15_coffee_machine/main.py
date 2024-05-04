from beverages import MENU, resources, coins


def process_coins(beverage):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total = (quarters * coins.get("quarters")) + (dimes * coins.get("dimes")) + (nickles * coins.get("nickles")) + (
            pennies * coins.get("pennies"))

    price = MENU[f"{beverage}"]["cost"]
    change = round(total - MENU[f"{beverage}"]["cost"], 2)

    if total >= price:
        print(f"Here is ${change} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")

    # return total


def check_resources(beverage):
    water = resources.get("water")
    milk = resources.get("milk")
    coffee = resources.get("coffee")

    if beverage == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml")
    elif water < MENU[f"{beverage}"]["ingredients"]["water"]:
        print(f"Sorry there is not enough {water}.")
    elif milk < MENU[f"{beverage}"]["ingredients"]["milk"]:
        print(f"Sorry there is not enough {milk}.")
    elif coffee < MENU[f"{beverage}"]["ingredients"]["coffee"]:
        print(f"Sorry there is not enough {coffee}.")
    else:
        if beverage == "espresso":
            water = water - MENU["espresso"]["ingredients"]["water"]
            milk = milk - MENU["espresso"]["ingredients"]["milk"]
            coffee = coffee - MENU["espresso"]["ingredients"]["coffee"]
            # print(water, milk, coffee)
        elif beverage == "latte":
            water = water - MENU["latte"]["ingredients"]["water"]
            milk = milk - MENU["latte"]["ingredients"]["milk"]
            coffee = coffee - MENU["latte"]["ingredients"]["coffee"]
            # print(water, milk, coffee)
        elif beverage == "cappuccino":
            water = water - MENU["cappuccino"]["ingredients"]["water"]
            milk = milk - MENU["cappuccino"]["ingredients"]["milk"]
            coffee = coffee - MENU["cappuccino"]["ingredients"]["coffee"]
            # print(water, milk, coffee)


turn_off = False

while not turn_off:
    chosen_beverage = input("What would you like? (espresso($1.50)/latte($2.5)/cappuccino($3.0)): ")

    if chosen_beverage == "off":
        turn_off = True
    else:
        check_resources(chosen_beverage)
        process_coins(chosen_beverage)
