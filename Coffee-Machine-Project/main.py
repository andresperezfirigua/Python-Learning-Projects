from Dict_Data import MENU
from Dict_Data import resources


def print_report(machine_money):
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {machine_money}")


def check_resources(drink):
    if MENU[drink]["ingredients"]["water"] <= resources["water"]:
        if MENU[drink]["ingredients"]["coffee"] <= resources["coffee"]:
            if drink == "espresso":
                return None
            elif MENU[drink]["ingredients"]["milk"] <= resources["milk"]:
                return None
            else:
                return "milk"
        else:
            return "coffee"
    else:
        return "water"


def prepare_order(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


def process_transaction(drink):
    payment = 0
    quarters = int(input("How many quarters?: "))
    payment += quarters * 0.25
    if payment >= MENU[drink]["cost"]:
        return payment
    dimes = int(input("How many dimes?: "))
    payment += dimes * 0.10
    if payment >= MENU[drink]["cost"]:
        return payment
    nickles = int(input("How many nickels?: "))
    payment += nickles * 0.05
    if payment >= MENU[drink]["cost"]:
        return payment
    pennies = int(input("How many pennies?: "))
    payment += pennies * 0.01
    if payment >= MENU[drink]["cost"]:
        return payment
    else:
        return -1


def turn_machine_on():
    serve_next_order = True
    machine_money = 0
    while serve_next_order:
        print(resources, machine_money)
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink in ["espresso", "latte", "cappuccino"]:
            if check_resources(drink) is None:
                inserted_money = process_transaction(drink)
                if inserted_money != -1:
                    prepare_order(drink)
                    machine_money += MENU[drink]['cost']
                    if inserted_money > MENU[drink]["cost"]:
                        print(f"Here's ${round(inserted_money - MENU[drink]['cost'], 2)} in change.")
                    print(f"Here's your {drink}. Enjoy!")
                else:
                    print(f"Sorry that's not enough money. Money refunded")
            else:
                print(f"Sorry there is not enough {check_resources(drink)}.")
        elif drink == "off":
            serve_next_order = False
        elif drink == "report":
            print_report(machine_money)
        else:
            print("Invalid option.")


turn_machine_on()
