from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    items = coffee_menu.get_items()
    order = input(f"What would you like? {items}:").lower()
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        print("Machine shutting down for maintenance.......")
        machine_on = False
    else:
        drink = coffee_menu.find_drink(order)
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources:
            print(drink.cost)
            sufficient_funds = money_machine.make_payment(drink.cost)
            if sufficient_funds:
                coffee_maker.make_coffee(drink)