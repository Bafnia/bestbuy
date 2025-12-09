from products import Product
from typing import List


class Store:
    def __init__(self, products: List[Product]):
        self.products = products[:]

    def add_product(self, product: Product):
        """Fügt ein Produkt zum Store hinzu"""
        if product not in self.products:
            self.products.append(product)

    def remove_product(self, product: Product):
        """Entfernt ein Produkt aus dem Store"""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Gibt die Gesamtmenge aller Produkte im Store zurück"""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Gibt eine Liste aller aktiven Produkte zurück"""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[tuple[Product, int]]) -> float:
        """
        Führt eine Bestellung aus.
        shopping_list: Liste von Tupeln (Produkt, gewünschte Menge)
        Gibt den Gesamtpreis der Bestellung zurück
        """
        if not shopping_list:
            return 0.0

        total_price = 0.0

        for product, quantity in shopping_list:
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
            total_price += product.buy(quantity)

        return total_price