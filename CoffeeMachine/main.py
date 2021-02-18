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
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels":0.05,
    "pennies": 0.01,

}
total_money = 0
moreCoffee = True
#enough_resources = ""
#customer_payment = []
def printResources():
    for resource in resources:
        print(f"{resource}: {resources[resource]} mL")
    print(f"Money: ${total_money}")
def checkResources(customer_choice):
    enough = ""
    for resource in MENU[customer_choice]["ingredients"]:
        #print(MENU[customer_choice]["ingredients"][resource])
        if resources[resource] < MENU[customer_choice]["ingredients"][resource]:
            enough = resource
    return enough
def depositCoins():
    payment = []
    for coin in coins:
        payment.append(int(input(f"How many {coin}?:")))
    return payment
def checkMoneys(current_payment, customer_choice):
    #enoughMoneys = 0
    total_payment = 0
    total_payment += current_payment[0] * 0.25
    total_payment += current_payment[1] * 0.10
    total_payment += current_payment[2] * 0.05
    total_payment += current_payment[3] * 0.01
    if total_payment < MENU[customer_choice]['cost']:
        #enoughMoneys = False
        return 0
    else:
        return total_payment
def checkout(total_payment, customer_choice):
    change = round(total_payment - MENU[customer_choice]['cost'],2)
    print(f"Here is your change: ${change}")
    print(f"Here is your {customer_choice}. Enjoy!!!")
    for resource in MENU[customer_choice]["ingredients"]:
        resources[resource] -= MENU[customer_choice]["ingredients"][resource]
    return MENU[customer_choice]['cost']

while moreCoffee:
    #TODO - ask customer what they would like
    choice = input("What would you like to order? (latte/cappuccino/espresso): ").lower()
    #TODO - make decision for choice
    if choice == 'q':
        moreCoffee = False
    elif choice != "report":
        # TODO - determine if there are enough resources
        enough_resources = checkResources(customer_choice=choice)
        #print(enough_resources)
        if enough_resources == "":
            customer_payment = depositCoins()
            print(customer_payment)
            enough_money = checkMoneys(customer_payment, choice)
            if enough_money > 0:
                total_money += checkout(total_payment=enough_money, customer_choice=choice)
            else:
                print(f"You did not deposit enough money")

        else:
            print(f"There isn't enough {enough_resources}")

    else:
        printResources()
     # TODO - receive payment

    #TODO - CHECK IF THERE IS ENOUGH MONEY
    #TODO - ADD TO TOTAL MONEY AND DISPENSE CHANGE


#printResources()