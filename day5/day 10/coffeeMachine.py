MENU = {
    "espresso": {
        "ingridients":{
        "water":50,
        "coffee":18,
    },
    "cost":1.5,
    },
    "latte": {
        "ingridients":{
        "water":200,
        "milk": 150,
        "coffee":24,
    },
    "cost":2.5,
    },
    "cappuccino":{
        "ingridients":{
        "water":250,
        "milk": 100,
        "coffee":24,
    },
    "cost":3.0 ,
    }
}
profit = 0
resource = {
    "water": 300,
    "milk":200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print("sorry there is not enough{item}.")
            return False
    return True 
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many pennies?: ")) * 0.01
    total += int(input("how many nickles?: ")) * 0.05
def is_transaction_successful(money_received, drink_cost):
    if  float(money_received) >= float(drink_cost):
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. money refunded.")
        return False 
def make_coffee(drink_name, order_ingridients):
    for item in order_ingridients:
        resource[item] -= order_ingridients[item]
    print(f"here is your {drink_name}.")
is_on = True

while True:
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resource['water']}ml")
        print(f"milk: {resource['milk']}ml")
        print(f"coffee: {resource['coffee']}ml")
        prin:(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingridients"]): 
            payment =  process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingridients"])
                