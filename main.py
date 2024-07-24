class VendingMachine:
    def __init__(self):
        self.drinks = {
            'Coke': 10,
            'Pepsi': 10,
            'Sprite': 8,
            '100Plus': 8,
            'PlainWater': 5
        }

        self.notes = [1, 5, 10, 20, 50, 100]

    def display_drinks(self):
        print("Available drinks:")
        for drink, price in self.drinks.items():
            print(f"{drink}: ${price}")

    def get_change(self, amount):
        change_notes = []
        for note in sorted(self.notes, reverse=True):
            while amount >= note:
                change_notes.append(note)
                amount -= note
        return change_notes

    def format_change(self, change_notes):
        note_count = {}
        for note in change_notes:
            if note in note_count:
                note_count[note] += 1
            else:
                note_count[note] = 1

        change_str_list = []
        for note, count in note_count.items():
            change_str_list.append(f"${note} x {count}")
        change_str = ", ".join(change_str_list)
        return change_str

    def purchase_drink(self, drink_choice, payment):
        drink_choice_normalized = drink_choice.lower()
        drinks_normalized = {k.lower(): v for k, v in self.drinks.items()}

        if drink_choice_normalized not in drinks_normalized:
            return "Sorry, the drink is not available."

        price = drinks_normalized[drink_choice_normalized]
        total_payment = payment

        while total_payment < price:
            print(f"Insufficient payment. {drink_choice} costs ${price}.")
            additional_payment = int(input("Please insert more money: "))
            while additional_payment not in self.notes:
                print("Invalid note. Please insert a valid note.")
                additional_payment = int(input("Please insert more money: "))
            total_payment += additional_payment

        change = total_payment - price
        if change == 0:
            return f"Here is your {drink_choice}. No change."
        else:
            change_notes = self.get_change(change)
            formatted_change = self.format_change(change_notes)
            return f"Here is your {drink_choice}. Your change is: {formatted_change}"


if __name__ == "__main__":
    vm = VendingMachine()
    vm.display_drinks()

    drink = input("Select your drink: ")
    drink_choice_normalized = drink.lower()
    drinks_normalized = {k.lower(): v for k, v in vm.drinks.items()}

    while drink_choice_normalized not in drinks_normalized:
        print("Sorry, the drink is not available.")
        drink = input("Select your drink: ")
        drink_choice_normalized = drink.lower()

    money = int(input("Insert money (in notes): "))
    while money not in vm.notes:
        print("Invalid note. Please insert a valid note.")
        money = int(input("Insert money (in notes): "))

    result = vm.purchase_drink(drink, money)
    print(result)
