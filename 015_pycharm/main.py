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


# TODO: # 1 Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: # 2 Turn off the Coffee Machine by entering "off" to the prompt.
if user_input == "off":
    print("Going Offline...")
# TODO: # 3 Print report
# When the user enters "report" to the prompt, a report should be generated that shows the current resource values
if user_input == "report":
    for key, value in resources.items():
        print("{} {}".format(key, value).title())
    print(f"Water: {resources['water']}ml")

# TODO: # 4 Check resources sufficient?
if user_input == "espresso":
    # check espresso with resources


# TODO: # 5 Process coins.

# TODO: # 6 Check transaction successful?

# TODO: # 7 Make Coffee

