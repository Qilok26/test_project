from restaurant import Restaurant
from menu_item import MenuItem

def display_menu():
    print("\nRestaurant Manager")
    print("1. View All")
    print("2. Search")
    print("3. Add")
    print("4. Update")
    print("5. Delete")
    print("6. Sort")
    print("7. Export")
    print("8. Exit")

def get_valid_input(prompt, validator=None):
    while True:
        value = input(prompt).strip()
        if validator is None or validator(value):
            return value
        print("Invalid input, please try again.")

def main():
    restaurant = Restaurant("data/restaurant_data.json")
    try:
        restaurant.load()
        print("Data loaded successfully.")
    except Exception as e:
        print("Error loading data: {}".format(e))  
        return
    
    while True:
        display_menu()
        choice = get_valid_input("Choose an option (1-8): ", lambda x: x in "12345678")
        
        if choice == "1":
            items = restaurant.list_items()
            if items:
                print("\nAll Menu Items:")
                for item in items:
                    status = "(In Stock)" if item.in_stock else "(Out of Stock)"
                    print(f"{item.id}: {item.name} ({item.category}) - ${item.price:.2f} {status}")
            else:
                print("No items found.")
        
        elif choice == "2":
            search_type = get_valid_input("Search by (name/category/id): ", lambda x: x in ["name", "category", "id"])
            if search_type == "id":
                id_str = get_valid_input("Enter ID: ", lambda x: x.isdigit())
                item = restaurant.search_by_id(int(id_str))
                if item:
                    print("\nFound: {0}: {1} - ${2:.2f}".format(item.id, item.name, item.price))
                else:
                    print("Item not found.")
            else:
                query = input("Enter {0}: ".format(search_type))
                results = (restaurant.search_by_name(query) if search_type == "name" 
                          else restaurant.search_by_category(query))
                if results:
                    print("\n{0} Search Results:".format(search_type.capitalize()))
                    for item in results:
                        print("{0}: {1} - ${2:.2f}".format(item.id, item.name, item.price))
                else:
                    print("No items found.")
        
        elif choice == "3":
            id_str = get_valid_input("Enter unique ID: ", lambda x: x.isdigit() and int(x) not in [item.id for item in restaurant.list_items()])
            name = get_valid_input("Enter name: ", lambda x: x != "")
            category = get_valid_input("Enter category: ", lambda x: x != "")
            price_str = get_valid_input("Enter price: ", lambda x: x.replace(".", "", 1).isdigit() and float(x) >= 0)
            item = MenuItem(int(id_str), name, category, float(price_str))
            if restaurant.add_item(item):
                print("Item added successfully.")
            else:
                print("Failed to add item (ID conflict).")
        
        elif choice == "4":
            id_str = get_valid_input("Enter ID to update: ", lambda x: x.isdigit())
            item = restaurant.get_item(int(id_str))
            if item:
                field = get_valid_input("Update (name/category/price/in_stock): ", lambda x: x in ["name", "category", "price", "in_stock"])
                if field == "price":
                    value = get_valid_input("New price: ", lambda x: x.replace(".", "").isdigit() and float(x) >= 0)
                    value = float(value)
                elif field == "in_stock":
                    value = get_valid_input("In stock (true/false): ", lambda x: x.lower() in ["true", "false"])
                    value = value.lower() == "true"
                else:
                    value = get_valid_input("New {0}: ".format(field), lambda x: x != "")
                if restaurant.update_item(int(id_str), field, value):
                    print("Item updated successfully.")
                else:
                    print("Update failed.")
            else:
                print("Item not found.")
        
        elif choice == "5":
            id_str = get_valid_input("Enter ID to delete: ", lambda x: x.isdigit())
            if restaurant.delete_item(int(id_str)):
                print("Item deleted successfully.")
            else:
                print("Item not found.")
        
        elif choice == "6":
            sort_by = get_valid_input("Sort by (name/price/availability): ",
                                    lambda x: x in ["name", "price", "availability"])
            reverse = get_valid_input("Order (asc/desc): ",
                                    lambda x: x in ["asc", "desc"]) == "desc"
            items = restaurant.sort_items(sort_by, reverse=reverse)

            if items:
                print("\nSorted Menu Items:")
                for item in items:
                    print("{0}: {1} ({2}) - ${3:.2f} {4}".format(
                        item.id, item.name, item.category, item.price,
                        '(In Stock)' if item.in_stock else '(Out of Stock)'))
            else:
                print("No items found.")
                
        elif choice == "7":
            items = restaurant.list_items()
            if items:
                fields = input("Fields to export (id,name,category,price,in_stock,comma-separated): ").split(",")
                filename = input("Enter filename (default: export.csv): ").strip() or "export.csv"
                try:
                    restaurant.export_items(items, fields, filename)
                    print(f"Exported to {filename}")
                except ValueError as e:
                    print(e)
            else:
                print("No items to export.")
        
        elif choice == "8":
            restaurant.save()
            print("Changes saved.")
            break

main()