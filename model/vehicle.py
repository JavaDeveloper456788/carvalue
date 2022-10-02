class Vehicle:
    year = None
    make = None
    model = None
    price = None
    mileage = None
    dealer_name = None
    dealer_street = None

    def __init__(self, year, make, model, price, mileage, dealer_name, dealer_street):
        self.year = year
        self.make = make
        self.model = model
        self.price = price
        self.mileage = mileage
        self.dealer_name = dealer_name
        self.dealer_street = dealer_street
