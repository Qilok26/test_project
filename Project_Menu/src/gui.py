from tkinter import Tk, Listbox, Button, END, simpledialog, messagebox
from restaurant import Restaurant

def main():
    app = Tk()
    app.title("Restaurant Manager")
    app.configure(bg="#1E3A5F")

    restaurant = Restaurant("data/restaurant_data.json")
    restaurant.load()

    listbox = Listbox(app, width=60, bg="#E0F0FF", fg="black", font=("Arial", 12))
    listbox.pack(pady=10)

    def refresh():
        listbox.delete(0, END)
        for item in restaurant.list_items():
            status = "(In Stock)" if item.in_stock else "(Out of Stock)"
            listbox.insert(END, f"{item.id}: {item.name} ({item.category}) - ${item.price:.2f} {status}")

    def search():
        query = simpledialog.askstring("Search", "Enter name or category:")
        if query:
            results = restaurant.search_by_name(query) + restaurant.search_by_category(query)
            listbox.delete(0, END)
            if results:
                for item in results:
                    listbox.insert(END, f"{item.id}: {item.name} - ${item.price:.2f}")
            else:
                messagebox.showinfo("Search", "No items found.")

    def add_item():
        name = simpledialog.askstring("Add Item", "Enter item name:")
        category = simpledialog.askstring("Add Item", "Enter category:")
        price = float(simpledialog.askstring("Add Item", "Enter price:"))
        in_stock = messagebox.askyesno("Add Item", "Is this item in stock?")
        restaurant.add_item(name, category, price, in_stock)
        refresh()

    def delete_item():
        id_str = simpledialog.askstring("Delete", "Enter ID to delete:")
        if id_str and id_str.isdigit():
            restaurant.delete_item(int(id_str))
            refresh()

    def update_item():
        id_str = simpledialog.askstring("Update", "Enter ID to update:")
        if id_str and id_str.isdigit():
            name = simpledialog.askstring("Update", "Enter new name (or leave blank):")
            category = simpledialog.askstring("Update", "Enter new category (or leave blank):")
            price_str = simpledialog.askstring("Update", "Enter new price (or leave blank):")
            in_stock = messagebox.askyesno("Update", "Is item in stock?")
            price = float(price_str) if price_str else None
            restaurant.update_item(int(id_str), name=name or None, category=category or None, price=price, in_stock=in_stock)
            refresh()

    def export():
        restaurant.save()
        messagebox.showinfo("Export", "Data exported successfully!")

    Button(app, text="View All", command=refresh, bg="#3B82F6", fg="white").pack(pady=2)
    Button(app, text="Search", command=search, bg="#3B82F6", fg="white").pack(pady=2)
    Button(app, text="Add", command=add_item, bg="#3B82F6", fg="white").pack(pady=2)
    Button(app, text="Update", command=update_item, bg="#3B82F6", fg="white").pack(pady=2)
    Button(app, text="Delete", command=delete_item, bg="#3B82F6", fg="white").pack(pady=2)
    Button(app, text="Export", command=export, bg="#3B82F6", fg="white").pack(pady=2)
    Button(app, text="Exit", command=app.destroy, bg="red", fg="white").pack(pady=5)

    app.mainloop()

if __name__ == "__main__":
    main()
