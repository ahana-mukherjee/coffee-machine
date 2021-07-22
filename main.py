MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

money_in_system = 0
is_on = True

def check_status(resources, MENU, response):
    #checks the status of the resources left
    for key in MENU[response]['ingredients']:
        if MENU[response]['ingredients'][key] > resources[key]:
            return key
        else:
            return True     

def calculate_change(response, quaters, dimes, nickles, pennies, MENU):
    #calculates the change
    money = (quaters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
    if money < MENU[response]['cost']:
        print("Sorry! Money not sufficient. Amount refunded.")
        return True
    else:    
        if response == 'espresso':
            change = money - 1.50
        elif response == 'latte':
            change = money - 2.50
        elif response == 'cappuccino':
            change = money - 3.00    
        return change           

def report(resources, money_in_system):
    #prints the report
    print(f"Water: {resources['water']}ml") 
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g") 
    print(f"Money: {money_in_system}")

while is_on:
    response = input("What would you like? (espresso/latte/cappuccino)\nFor report, type 'report'.\nTo turn the machine off, type 'off': ").lower()
    if response == 'report':
        report(resources, money_in_system)
    elif response == 'off':
        is_on = False
        continue     
    elif check_status(resources, MENU, response) == True:
        print("Please insert coins.")
        quaters = int(input("How many quaters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        resources['water'] -= MENU[response]['ingredients']['water']
        resources['coffee'] -= MENU[response]['ingredients']['coffee']
        resources['milk'] -= MENU[response]['ingredients']['milk']

        change = calculate_change(response, quaters, dimes, nickles, pennies, MENU)
        money_in_system += MENU[response]['cost']
        if change == True:
            continue
        else:
            print(f"Here is your ${'{:.1f}'.format(change)} change.")
            print(f"Here is your {response}. Enjoy!")   
    else:
        print(f"Sorry! Not enough {check_status(resources, MENU, response)}.")    
    