
from pathlib import Path
import json
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
                item = MenuItem(
                    id=it["id"],
                    name=it["name"],
                    category=cat_name,                 # bring category down
                    price=it["price"],
                    calories=it.get("calories", ""),
                    protein=it.get("protein", ""),
                    spice_lvl=it.get("spice_lvl", ""),
                    in_stock=it.get("in_stock", True)  # map boolean correctly
                )
                self._items_by_id[int(item.id)] = item

    def save(self):
        """Save back to the nested JSON structure, grouping by category."""
        # group items by category
        by_cat: Dict[str, List[MenuItem]] = {}
        for it in self._items_by_id.values():
            by_cat.setdefault(it.category, []).append(it)

        # rebuild 'menu' array; assign simple category ids 1..N
        menu = []
        for idx, (cat_name, items) in enumerate(by_cat.items(), start=1):
            menu.append({
                "category": cat_name,
                "id": idx,
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
        return list(self._items_by_id.values())

    def get_item(self, id: int) -> Optional[MenuItem]:
        return self._items_by_id.get(int(id))

    # -------- CRUD --------
    def add_item(self, item: MenuItem) -> bool:
        iid = int(item.id)
        if iid in self._items_by_id:
            return False
        self._items_by_id[iid] = item
        return True

    def update_item(self, id: int, field: str, value) -> bool:
        it = self.get_item(id)
        if not it:
            return False
        it.update(field, value)
        return True

    def delete_item(self, id: int) -> bool:
        return self._items_by_id.pop(int(id), None) is not None

    # -------- search --------
    def search_by_id(self, id: int) -> Optional[MenuItem]:
        return self.get_item(id)

    def search_by_name(self, text: str) -> List[MenuItem]:
        q = text.strip().lower()
        return [it for it in self._items_by_id.values() if q in it.name.lower()]

    def search_by_category(self, category: str) -> List[MenuItem]:
        q = category.strip().lower()
        return [it for it in self._items_by_id.values() if it.category.lower() == q]

