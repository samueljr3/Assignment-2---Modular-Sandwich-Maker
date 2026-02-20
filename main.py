import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    isOn = True
    while isOn:
        user_choice = input("What would you like? (small/medium/large/off/): ")
        if user_choice == "off":
            isOn = False
        elif user_choice == "small" or user_choice == "medium" or user_choice == "large":
            if sandwich_maker_instance.check_resources(recipes[user_choice]["ingredients"]):
                paymentTotal = cashier_instance.process_coins()
                if cashier_instance.transaction_result(paymentTotal, recipes[user_choice]["cost"]):
                    sandwich_maker_instance.make_sandwich(user_choice, recipes[user_choice]["ingredients"])


if __name__=="__main__":
    main()