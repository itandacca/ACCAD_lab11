
menu = {
    1: ("Adobo", 100.00),
    2: ("Sinigang na Baboy", 120.00),
    3: ("Pancit Canton", 90.00),
    4: ("Halo-Halo", 50.00),
    5: ("Kare-Kare", 110.00),
    6: ("Lechon", 150.00),
    7: ("Balut", 70.00),
    8: ("Taho", 30.00)
}


def display_menu():
    print("\nWelcome to the Food Ordering System!")
    print("--- Our Filipino Menu ---")
    for key in menu:
        item, price = menu[key]
        print(f"{key}. {item} - PHP {price}")


def take_order():
    while True:
        try:
            choice = int(input("\nEnter the number of the item you'd like to order: "))
            if choice in menu:
                item, price = menu[choice]
                print(f"You selected {item} which costs ${price}")
                return price
            else:
                print("Invalid choice. Please select a valid number from the menu.")
        except ValueError:
            print("Please enter a valid number.")


def process_payment(total):
    while True:
        try:
            cash = float(input(f"\nTotal cost: PHP {total}. Enter cash: PHP "))
            if cash < total:
                print("Not enough cash. Please give more money.")
            else:
                change = cash - total
                print(f"Payment successful. Your change is PHP {change:.2f}")
                return
        except ValueError:
            print("Invalid amount. Please enter a valid number.")


def main():
    display_menu()
    total_cost = take_order()
    process_payment(total_cost)

if __name__ == "__main__":
    main()
