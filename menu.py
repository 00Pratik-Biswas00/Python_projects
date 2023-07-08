MENU = {
    "green tea": {
        "ingredients": {
            "water": 240,
            "tea_leaves": 1,
        },
        "cost": 95,
    },
    "assam tea": {
        "ingredients": {
            "water": 600,
            "milk": 120,
            "tea_leaves": 0.5,
        },
        "cost": 110,
    },
    "darjeeling tea": {
        "ingredients": {
            "water": 240,
            "milk": 160,
            "tea_leaves": 2,
        },
        "cost": 75,
    }
}

profit = 0

resources = {
    "water": 5000,
    "milk": 500,
    "tea_leaves": 30,
}


def sufficient_resources(order_ingredients):
    for items in order_ingredients:
        if resources[items] < order_ingredients[items]:
            print(f"Sorry there is not enough {items} ")
            return False
    return True


def process_coins():
    print("Please insert coins: ")
    total = int(input("Enter number of ₹1 coins: ")) * 1
    total += int(input("Enter number of ₹2 coins: ")) * 2
    total += int(input("Enter number of ₹5 coins: ")) * 5
    total += int(input("Enter number of ₹10 notes: ")) * 10
    total += int(input("Enter number of ₹20 notes: ")) * 20
    total += int(input("Enter number of ₹50 notes: ")) * 50
    total += int(input("Enter number of ₹100 notes: ")) * 100
    return total


def successful_transaction(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round((money_recieved - drink_cost), 2)
        print(f"Here is the ₹ {change} change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name} ☕. Enjoy!")


is_on = True

while is_on:
    choice = input(
        "What would you like? (Green tea/Assam tea/Darjeeling tea) | If you don't want anything write Off | If you want to see the available resources then write Report: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(
            f"Resources we currently have:\nWater: {resources['water']} ml\nMilk: {resources['milk']} ml\nTea leaves: {resources['tea_leaves']} tablespoon\nProfit till now: ₹ {profit}\n")
    else:
        drink = MENU[choice]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
