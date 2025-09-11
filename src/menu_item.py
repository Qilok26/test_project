
from typing import Any, Dict


class MenuItem:
    def __init__(self, id: int, name: str, category: str,
                 price: float, calories: Any = "", protein: Any = "",
                 spice_lvl: Any = "", in_stock: bool = True):
        self.id = int(id)
        self.name = name
        self.category = category
        self.price = float(price)
        # allow numbers or strings, since JSON may contain either
        self.calories = calories
        self.protein = protein
        self.spice_lvl = spice_lvl
        self.in_stock = bool(in_stock)

    def to_dict(self) -> Dict[str, Any]:
        # Keys match the attributes (including in_stock)
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "calories": self.calories,
            "protein": self.protein,
            "spice_lvl": self.spice_lvl,
            "in_stock": self.in_stock,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "MenuItem":
        # Read 'in_stock' from your JSON (not 'availability')
        return MenuItem(
            d["id"],
            d["name"],
            d["category"],
            d["price"],
            d.get("calories", ""),
            d.get("protein", ""),
            d.get("spice_lvl", ""),
            d.get("in_stock", True),
        )

    def update(self, field: str, value: Any) -> None:
        if hasattr(self, field):
            setattr(self, field, value)

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f}"








