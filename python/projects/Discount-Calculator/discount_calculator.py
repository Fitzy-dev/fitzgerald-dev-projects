# Jordan Fitzgerald
# 4/6/2026
# Updated Discount Calculator Project

from abc import ABC, abstractmethod # Importing ABC and abstractmethod to create an abstract base class for discount strategies

class Product: # Product class represents an item with a name and price, and includes a string representation for easy display
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'

class DiscountStrategy(ABC): # Abstract base class for discount strategies, defining the interface for checking applicability and applying discounts to products
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass

class PercentageDiscount(DiscountStrategy): # PercentageDiscount class implements a discount strategy that applies a percentage-based discount to the product price, and checks if the discount is applicable based on the percentage value
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy): # FixedAmountDiscount class implements a discount strategy that applies a fixed amount discount to the product price, and checks if the discount is applicable based on the product price and the fixed amount
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount

class PremiumUserDiscount(DiscountStrategy): # PremiumUserDiscount class implements a discount strategy that applies a 20% discount for premium users, and checks if the discount is applicable based on the user's tier
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8

class DiscountEngine: # DiscountEngine class takes a list of discount strategies and calculates the best price for a product based on the applicable discounts, by comparing the original price with the discounted prices and returning the lowest one
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)

def main(): # Main function to demonstrate the discount calculator by creating a product, defining user tier, and applying multiple discount strategies to calculate and display the best price for the product based on the applicable discounts
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'

    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)
    print(f"Best price for {product.name} for {user_tier} user: ${best_price:.2f}")    

if __name__ == "__main__":
    main()
