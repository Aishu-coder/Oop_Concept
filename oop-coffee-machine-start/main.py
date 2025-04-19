from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine=CoffeeMaker()
money=MoneyMachine()
menu=Menu()
is_on=True
while is_on:
    order=input("what would you like to have?"+menu.get_items())
    if order=="report":
        coffee_machine.report()
        money.report()
    elif order=="off":
        is_on=False
    else :
        drink=menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)