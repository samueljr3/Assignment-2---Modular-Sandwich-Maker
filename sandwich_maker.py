class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")