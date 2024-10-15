"""Following is the data of vehicles and customers with their respective attributes. This data is to be gotten from a json
file and then converted to respective objects but all that is being done here"""
vehicles = [
    {"vehicle_id": "MRT01", "make": 'Toyota', "model": "V1", "year": "2020", "rental_rate": 2000, "availability": True, "type":'R'},
    {"vehicle_id": "MRT02", "make": 'Honda', "model": "V1", "year": "2021", "rental_rate": 2000, "availability": True, "type":'R'},
    {"vehicle_id": "MRT03", "make": 'Toyota', "model": "V1", "year": "2019", "rental_rate": 2000, "availability": True, "type":'R'},
    {"vehicle_id": "MRT04", "make": 'Hyundai', "model": "V1", "year": "2014", "rental_rate": 1500,
     "availability": True, "type":'R'},
    {"vehicle_id": "MRT05", "make": 'Kia', "model": "V1", "year": "2022", "rental_rate": 3000, "availability": True, "type":'R'},
    {"vehicle_id": "MRT06", "make": 'Toyota', "model": "V2", "year": "2021", "rental_rate": 2500, "availability": True, "type":'R'},
    {"vehicle_id": "MRT07", "make": 'Maruti', "model": "V1", "year": "2018", "rental_rate": 1000, "availability": True, "type":'R'},
    {"vehicle_id": "MRT08", "make": 'Mercedes', "model": "V1", "year": "2021", "rental_rate": 5000,
     "availability": True, "type":'L', "extra_features":'GPS'},
    {"vehicle_id": "MRT09", "make": 'Mercedes', "model": "V2", "year": "2022", "rental_rate": 7000,
     "availability": True, "type":'L', "extra_features":'GPS'},
    {"vehicle_id": "MRT10", "make": 'Audi', "model": "V1", "year": "2023", "rental_rate": 10000, "availability": True, "type":'L', "extra_features":'GPS'},
    ]

customers =[
    {"c_id": "C01", "name":"Rahul", "contact_info":"rahul@xyz.com", "rental_history":{"#1":["MRT01", 10], "#2":["MRT03", 15],}, 'type':"R"},
    {"c_id": "C02", "name":"Abhay", "contact_info":"abhay@xyz.com", "rental_history":{"#1":["MRT04", 40], "#2":["MRT01", 1], 'type':"R"}},
    {"c_id": "C03", "name":"Rajesh", "contact_info":"rajesh@xyz.com", "rental_history":{"#1":["MRT09", 20], "#2":["MRT02", 105], 'type':"P"}}
]

class Vehicle:
    vehicle_type = 'Car'

    def __init__(self, vehicle_id, make, model, year, rental_rate, availability):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.availability = availability

    def print_vehicle(self):
        print(f"Your vehicle is : {self.vehicle_id}")
        print(f"Its Make is : {self.make}")
        print(f"Its Model is : {self.model}")
        print(f"Its Year of manufacture is : {self.year}")
        print(f"Its Rental Rate is : {self.rental_rate}")
        print(f"Its Availability is : {self.availability}")

    def rent_vehicle(self, c_id, rental_duration):
        rent = self.rental_rate * rental_duration
        if self.availability:
            self.availability = False
            print(f"Dear Customer, Thank you for choosing MRT Rentals.")
            print(f"Your Rental Rate is : {rent}")
            print(f"Your Customer ID is : {c_id}")
        else:
            print("Dear Customer, Unfortunately the vehicle you are opting for is unavailable.")

    def return_vehicle(self):
        self.availability = True
        print(f"Your vehicle has been successfully returned.")
        print(f"Thank you for choosing MRT Rentals.")


class LuxuryVehicle(Vehicle):
    def __init__(self, vehicle_id, make, model, year, rental_rate, availability, extra_features):
        super().__init__(vehicle_id, make, model, year, rental_rate, availability)
        self.extra_features = extra_features
        self.rental_rate = rental_rate + rental_rate * 0.2


class Customer:
    def __init__(self, c_id, name, contact_info, rental_history):
        self.c_id = c_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = rental_history

    def print_customer(self):
        print(f"Hello dear customer ! ")
        print(f"Your Customer ID is : {self.c_id}")
        print(f"Your Name is : {self.name}")
        print(f"Your Contact Info is : {self.contact_info}")

    def view_history(self):
        print(f"Hello dear customer ! ")
        print(f"Your Customer ID is : {self.c_id}")
        print(f"Your Rental history is : {self.rental_history}")


class RegularCustomer(Customer):
    def __init__(self, c_id, name, contact_info, rental_history):
        super().__init__(c_id, name, contact_info, rental_history)


class PremiumCustomer(Customer):
    def __init__(self, c_id, name, contact_info, rental_history):
        super().__init__(c_id, name, contact_info, rental_history)

    def apply_discount(self, rent):
        final_rent = rent - 0.1 * rent
        print(f"Your Discount is : {0.1 * rent}")
        print(f"Your Final Rent is : {final_rent}")


class RentalManager:
    def list_vehicles(self):
        for i in vehicles:
            if i["availability"]:
                print(f"{i['vehicle_id']} : {i['make']} : {i['model']}")

    def add_vehicle(self, vehicle_id, make, model, year, rental_rate, availability):
        vehicles.append({"vehicle_id": vehicle_id, "make": make, "model": model, "year": year, rental_rate: rental_rate, "availability": availability})

    def remove_vehicle(self, vehicle_id):
        vehicles.remove({"vehicle_id": vehicle_id})

    def generate_report(self):
        print(f"Vehicles In Use Report:")
        for vehicle in vehicles:
            if not(vehicle[("availability")]):
                print(f"{vehicle['vehicle_id']} : {vehicle['make']} : {vehicle['model']}")
        print("Customer report")
        for customer in customers:
            print(f"{customer['c_id']} : {customer['name']} : {customer['contact_info']}, {customer['rental_history']}")




if __name__ == "__main__":
    cars = list()
    people = list()
    for vehicle in vehicles:
        if vehicle['type'] == 'R':
            cars.append(Vehicle(vehicle["vehicle_id"], vehicle["make"], vehicle["model"], vehicle["year"], vehicle["rental_rate"], vehicle["availability"]))
        else:
            cars.append(LuxuryVehicle(vehicle["vehicle_id"], vehicle["make"], vehicle["model"], vehicle["year"], vehicle["rental_rate"], vehicle["availability"], vehicle["extra_features"]))

    for customer in customers:
        if customer['type'] == 'R':
            people.append(RegularCustomer(customer["c_id"], customer["name"], customer["contact_info"], customer["rental_history"]))
        else:
            people.append(PremiumCustomer(customer["c_id"], customer["name"], customer["contact_info"], customer["rental_history"]))



