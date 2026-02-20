class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
       while True:
            try:
                total = 0.0
                print("Please insert coins.")
                total += float(input("how many large dollars?: "))
                total += float(input("how many half dollars?: ")) * 0.5
                total += float(input("how many quarters?: ")) * 0.25
                total += float(input("how many nickles?: ")) * 0.05
                return total
            except ValueError:
                print("Please only enter numbers and try again. Your money has been returned.")

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False