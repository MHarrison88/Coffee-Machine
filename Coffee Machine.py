MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER = .25
DIME = .1
NICKEL = .05
PENNY = .01

refund = 0
cost = 0
bank = 0
coffee_machine = True

def report():
    """Prints a report of the resources and money in the machine"""
    print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney in the machine: ${bank} ")

def vend(drink):
    """Subtracts the resources used for the drink from the machine"""
    for each in drink:
        resources[each] -= drink[each]


def check_resources(ingredients):
    """Checks to make sure enough ingredients are in the machine"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print("Not enough ingredients")
            return False
    return True

def pay():
    """Calculates payment entered"""
    payment = 0
    q = float(input("How many quarters?: "))
    d = float(input("How many dimes?: "))
    n = float(input("How many nickels?: "))
    p = float(input("How many pennies?: "))
    payment += q * QUARTER
    payment += d * DIME
    payment += n * NICKEL
    payment += p * PENNY

    return payment

while coffee_machine:
    print(f"Espresso: ${MENU['espresso']['cost']}, Latte: ${MENU['latte']['cost']}, Cappucino: ${MENU['cappuccino']['cost']}")
    choice = input("Which drink would you like? 'espresso', 'latte', or 'cappuccino': ?\n").lower()

    if choice == "off":
        coffee_machine = False

    elif choice == "report":
        report()

    elif choice == "espresso":
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            cost = drink['cost']
            payment = pay()
            change = round(payment - cost, 2)

            if payment < cost:
                print("That is not enough, money refunded")
            else:
                bank += cost
                print(f"Here is ${change} in change.")
                print(f"Enjoy your {choice}!")
                vend(drink['ingredients'])

    elif choice == "latte":
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            cost = drink['cost']
            payment = pay()
            change = round(payment - cost, 2)

            if payment < cost:
                print("That is not enough, money refunded")
            else:
                bank += cost
                print(f"Here is ${change} in change.")
                print(f"Enjoy your {choice}!")
                vend(drink['ingredients'])

    elif choice == "cappuccino":
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            cost = drink['cost']
            payment = pay()
            change = round(payment - cost, 2)

            if payment < cost:
                print("That is not enough, money refunded")
            else:
                bank += cost
                print(f"Here is ${change} in change.")
                print(f"Enjoy your {choice}!")
                vend(drink['ingredients'])