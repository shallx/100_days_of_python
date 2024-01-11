from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


end = False
while not end:
    userChoice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if userChoice == "report":
        print(coffeeMaker.report())
    elif userChoice == "off":
        end = True
    elif userChoice in [item.name for item in menu.menu]:
        item = menu.find_drink(userChoice)
        if coffeeMaker.is_resource_sufficient(item):
            if moneyMachine.make_payment(item.cost):
                coffeeMaker.make_coffee(item)
    else:
        print("Invalid Choice, try again!")
