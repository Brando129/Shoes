# Build a class for storing data for a shoe management comapny. Shoe
# should have a brand, type, price, and status of in stock or not.

# Go On Sale: Cut a particular shoe's price by a certain percent for a special sale
# Add Tax: Calculate the total including tax, when a customer buys a new pair of that kind of shoe
# Cut the price by a certain amount of money (but not so it's negative!)
# Hike the Price: Increase the price by a certain amount.

class shoe:

    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1 - percent_off)

    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total

    def cut_price_by(self, amount):
        if amount < self.price:
            self.price -= amount
        else:
            print("Price deduction too large.")



skater_shoe = shoe("Vans", "Low-top Tainers", 59.99)
dress_shoe = shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
my_shoe = shoe("Converse", "Low-tops", 36.00)
print(my_shoe.total_with_tax(0.05))
my_shoe.cut_price_by(10)
print(my_shoe.price)
print(skater_shoe.type)
print(dress_shoe.type)


