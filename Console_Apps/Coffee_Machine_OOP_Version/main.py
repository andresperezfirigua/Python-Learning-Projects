from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


def turn_on():
    usr_input = ""
    while usr_input != "off":
        usr_input = input(f"What would you like? ({menu.get_items()[:-1]}): ").lower()
        if usr_input == "report":
            coffeeMaker.report()
            moneyMachine.report()
        elif usr_input != "off":
            drink = menu.find_drink(usr_input)
            if drink is not None:
                if coffeeMaker.is_resource_sufficient(drink):
                    if moneyMachine.make_payment(drink.cost):
                        coffeeMaker.make_coffee(drink)


turn_on()
