from pathlib import Path
import json
import csv
from typing import Optional, Dict, List
from menu_item import MenuItem



class Restaurant:
    def __init__(self, json_path):
        self.json_path = Path(json_path)
        self._items_by_id: Dict[int, MenuItem] = {}
        # keep the top-level metadata from your nested JSON
        self.meta = {"name": "", "location": "", "cuisine": ""}

    # -------- persistence (for NESTED JSON) --------
    def load(self):
        """Load nested JSON: {name, location, cuisine, menu:[{category, id, items:[...]}, ...]}."""
        try:
            root = json.loads(self.json_path.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            root = {"name": "", "location": "", "cuisine": "", "menu": []}

        self.meta["name"] = root.get("name", "")
        self.meta["location"] = root.get("location", "")
        self.meta["cuisine"] = root.get("cuisine", "")

        self._items_by_id = {}
        for cat in root.get("menu", []):
            cat_name = cat.get("category", "")
            for it in cat.get("items", []):
                # inject category into dict before calling from_dict
                item_dict = {**it, "category": cat_name}
                item = MenuItem.from_dict(item_dict)
                self._items_by_id[int(item.id)] = item

    def save(self):
        """Save back to the nested JSON structure, grouping by category."""
        # group items by category
        by_cat: Dict[str, List[MenuItem]] = {}
        for it in self._items_by_id.values():
            by_cat.setdefault(it.category, []).append(it)

        # rebuild 'menu' array; assign simple category ids 1..N
        menu = []
        for cat_name, items in by_cat.items():
            cat_id = len(menu) + 1  # just assign sequential ids

            menu.append({
                "category": cat_name,
                "id": cat_id,
                "items": [
                    {
                        "id": it.id,
                        "name": it.name,
                        "price": it.price,
                        "calories": it.calories,
                        "protein": it.protein,
                        "spice_lvl": it.spice_lvl,
                        "in_stock": it.in_stock,
                    }
                    for it in items
                ]
            })

        root = {
            "name": self.meta.get("name", ""),
            "location": self.meta.get("location", ""),
            "cuisine": self.meta.get("cuisine", ""),
            "menu": menu
        }
        self.json_path.parent.mkdir(parents=True, exist_ok=True)
        self.json_path.write_text(json.dumps(root, indent=2), encoding="utf-8")

    # -------- basic access --------
    def list_items(self) -> List[MenuItem]:
        return sorted(self._items_by_id.values(), key=lambda x: x.id)


    def get_item(self, id: int) -> Optional[MenuItem]:
        return self._items_by_id.get(int(id))

    # -------- CRUD --------
    def add_item(self, name: str, category: str, price: float, in_stock: bool):
        if not name.strip():
            raise ValueError("Item name cannot be empty")
        if not category.strip():
            raise ValueError("Category cannot be empty")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

        new_id = max(self._items_by_id.keys(), default=0) + 1
        item = MenuItem(new_id, name, category, price, in_stock)
        self._items_by_id[new_id] = item
        return item

    def update_item(self, item_id: int, **kwargs):
        if item_id not in self._items_by_id:
            raise ValueError(f"Item with ID {item_id} does not exist")
        item = self._items_by_id[item_id]
        for key, value in kwargs.items():
            if value is not None:
                setattr(item, key, value)
        return item

    def delete_item(self, item_id: int):
        if item_id not in self._items_by_id:
            raise ValueError(f"Item with ID {item_id} does not exist")
        del self._items_by_id[item_id]

    # -------- search --------
    def search_by_id(self, id: int) -> Optional[MenuItem]:
        return self.get_item(id)

    def search_by_name(self, text: str) -> List[MenuItem]:
        q = text.strip().lower()
        return [it for it in self._items_by_id.values() if q in it.name.lower()]

    def search_by_category(self, category: str) -> List[MenuItem]:
        q = category.strip().lower()
        return [it for it in self._items_by_id.values() if it.category.lower() == q]
    
    #Added better sorting here
    def sort_items(self, sort_by: str, reverse: bool = False):
        if sort_by == "name":
            return sorted(self._items_by_id.values(), key=lambda x: x.name.lower(), reverse=reverse)
        elif sort_by == "price":
            return sorted(self._items_by_id.values(), key=lambda x: x.price, reverse=reverse)
        elif sort_by == "availability":
            return sorted(self._items_by_id.values(), key=lambda x: x.in_stock, reverse=reverse)
        else:
            return []
        
    #Added export items, for the advanced
    def export_items(self, items, fields, filename="export.csv"):
        valid_fields = [f for f in fields if f in ["id", "name", "category", "price", "in_stock"]]
        if not valid_fields:
            raise ValueError("No valid fields selected")

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(valid_fields)  
            for item in items:
                writer.writerow([getattr(item, f) for f in valid_fields])



