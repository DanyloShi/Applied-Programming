class FirearmStore:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._inventory = {}

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise ValueError("Location must be a string.")
        self._location = value

    def add_firearm(self, firearm_type, quantity):
        if not FirearmStore.validate_quantity(quantity):
            raise ValueError("Invalid quantity.")
        if firearm_type in self._inventory:
            self._inventory[firearm_type] += quantity
        else:
            self._inventory[firearm_type] = quantity
        return f"Added {quantity} {firearm_type}(s) to inventory."

    def sell_firearm(self, firearm_type, quantity):
        if not FirearmStore.validate_quantity(quantity):
            raise ValueError("Invalid quantity.")
        if self._inventory.get(firearm_type, 0) >= quantity:
            self._inventory[firearm_type] -= quantity
            return f"Sold {quantity} {firearm_type}(s)."
        return "Not enough firearms in inventory."

    @staticmethod
    def validate_quantity(quantity):
        return isinstance(quantity, int) and quantity > 0

    def __str__(self):
        return f"FirearmStore: {self._name} in {self._location}"

class SpecializedFirearmStore(FirearmStore):
    def __init__(self, name, location, specialty):
        super().__init__(name, location)
        self.specialty = specialty

    def provide_demo(self, firearm_type):
        if firearm_type in self._inventory and self._inventory[firearm_type] > 0:
            return f"Providing a demonstration for {firearm_type}."
        return f"No {firearm_type} available for demo."

    def __str__(self):
        return f"SpecializedFirearmStore: {self.name} in {self.location}, Specializes in {self.specialty}"

class Discount:
    def apply_discount(self, price, discount):
        return price - (price * discount / 100)

class DiscountedFirearmStore(FirearmStore, Discount):
    def sell_firearm_with_discount(self, firearm_type, quantity, discount):
        if self._inventory.get(firearm_type, 0) >= quantity:
            self._inventory[firearm_type] -= quantity
            price = 100  # Припустимо, що ціна за одиницю 100
            discounted_price = self.apply_discount(price, discount)
            return f"Sold {quantity} {firearm_type}(s) with discount. Total: {discounted_price * quantity}"
        return "Not enough firearms in inventory."

if __name__ == "__main__":
    store = FirearmStore("Lviv Hunter", "Lviv, UA")
    specialized_store = SpecializedFirearmStore("Special Ops Lviv", "Lviv, UA", "Tactical Weapons")
    discounted_store = DiscountedFirearmStore("Discount Guns Lviv", "Lviv, UA")

    print(store)
    print(store.add_firearm("Rifle", 20))
    print(store.sell_firearm("Rifle", 2))

    print(specialized_store)
    print(specialized_store.add_firearm("Sniper Rifle", 5))
    print(specialized_store.provide_demo("Sniper Rifle"))

    print(discounted_store)
    print(discounted_store.sell_firearm_with_discount("Rifle", 1, 10))