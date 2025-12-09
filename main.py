from products import Product
from store import Store


# -------------------------------------------------
# Initiales Inventar – genau wie in der Aufgabe gefordert
# -------------------------------------------------
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = Store(product_list)


# -------------------------------------------------
# Benutzeroberfläche
# -------------------------------------------------
def start(store: Store):
    while True:
        print("\n" + "="*40)
        print("         Best Buy Store Menu")
        print("="*40)
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print("-"*40)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\n------ All Active Products ------")
            active_products = store.get_all_products()
            if not active_products:
                print("No active products available.")
            else:
                for product in active_products:
                    product.show()

        elif choice == "2":
            total = store.get_total_quantity()
            print(f"\nTotal number of items in store: {total}")

        elif choice == "3":
            print("\n------ Make an Order ------")
            active_products = store.get_all_products()
            if not active_products:
                print("No active products to order.")
                continue

            # Zeige verfügbare Produkte mit Index
            for idx, product in enumerate(active_products):
                print(f"{idx}. ", end="")
                product.show()

            try:
                shopping_list = []
                while True:
                    user_input = input("\nEnter product index and quantity (e.g. '0 2') or press Enter to finish: ").strip()
                    if user_input == "":
                        break
                    parts = user_input.split()
                    if len(parts) != 2:
                        print("Please enter index and quantity separated by space.")
                        continue
                    idx, qty = int(parts[0]), int(parts[1])
                    if idx < 0 or idx >= len(active_products):
                        print("Invalid product index.")
                        continue
                    if qty <= 0:
                        print("Quantity must be positive.")
                        continue
                    shopping_list.append((active_products[idx], qty))

                if not shopping_list:
                    print("Order cancelled – no items selected.")
                else:
                    total_price = store.order(shopping_list)
                    print(f"\nOrder placed successfully!")
                    print(f"Total cost: {total_price:.2f} dollars")

            except Exception as e:
                print(f"Error processing order: {e}")

        elif choice == "4":
            print("\nThank you for visiting Best Buy! Goodbye")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# -------------------------------------------------
# Programm starten
# -------------------------------------------------
if __name__ == "__main__":
    start(best_buy)