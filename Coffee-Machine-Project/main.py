from Dict_Data import MENU
from Dict_Data import resources


def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    payment = 0
    print("Please insert coins")
    for coin in coins:
        inserted_coins = int(input(f"How many {coin}?: "))
        payment += inserted_coins * coins[coin]
    return payment


def check_transaction(payment, drink):
    drink_cost = MENU[drink]["cost"]
    if payment > drink_cost:
        print(f"Here is ${round(payment - drink_cost, 2)} dollars in change.")
        return True
    elif payment == drink_cost:
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy!")


def print_report(machine_money):
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${machine_money}")


def turn_on():
    user_input = ""
    machine_money = 0
    while user_input != "off":
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input in ["espresso", "latte", "cappuccino"]:
            if check_resources(user_input):
                payment = process_coins()
                if check_transaction(payment, user_input):
                    machine_money += MENU[user_input]["cost"]
                    make_coffee(user_input)
        elif user_input == "report":
            print_report(machine_money)
        else:
            print("Invalid option")


turn_on()
