'''
PROTOTYPE OF CAR RENTAL SYSTEM


PROJECT TO TEST OOP UNDERSTANDING

'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_rented = False  # Initially, the car is not rented.

    def rent(self):
        if self.is_rented:
            print(f"The car {self.make} {self.model} is already rented.")
        else:
            self.is_rented = True
            print(f"The car {self.make} {self.model} has been rented.")

    def return_car(self):
        if not self.is_rented:
            print(f"The car {self.make} {self.model} was not rented.")
        else:
            self.is_rented = False
            print(f"The car {self.make} {self.model} has been returned.")

    def display_info(self):
        rental_status = "Rented" if self.is_rented else "Available"
        print(f"Car: {self.year} {self.make} {self.model} | Status: {rental_status}")


class Customer:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
        self.rented_car = None  # Initially, the customer hasn't rented a car.

    def rent_car(self, car):
        if self.rented_car is not None:
            print(f"{self.name} has already rented a car.")
        elif car.is_rented:
            print(f"Sorry, {car.make} {car.model} is already rented.")
        else:
            car.rent()  # Mark the car as rented.
            self.rented_car = car
            print(f"{self.name} has rented the car {car.make} {car.model}.")

    def return_car(self):
        if self.rented_car is None:
            print(f"{self.name} has not rented any car to return.")
        else:
            self.rented_car.return_car()  # Mark the car as returned.
            print(f"{self.name} has returned the car {self.rented_car.make} {self.rented_car.model}.")
            self.rented_car = None


# Testing the Car Rental System
if __name__ == "__main__":
    # Create some cars
    car1 = Car("Mahindra", "XUV", 2025)
    car2 = Car("Maruti Suzuki", "800", 2021)

    # Create a customer
    customer1 = Customer("customer_xyz", "XYZ123")

    # Display car info
    car1.display_info()
    car2.display_info()

    # Alice rents car1
    customer1.rent_car(car1)

    # Try renting the already rented car1
    customer1.rent_car(car1)  # Should print an error message.

    # Try renting another car while already renting one
    customer1.rent_car(car2)  # Should print an error message.

    # Display car info again
    car1.display_info()
    car2.display_info()

    # customer_1 returns car1
    customer1.return_car()

    # Try returning a car again (when none is rented)
    customer1.return_car()  # Should print an error message.

    # Rent a second car
    customer1.rent_car(car2)

    # Display updated car info
    car1.display_info()
    car2.display_info()
