"""Following is the data of vehicles and customers with their respective attributes. This data is to be gotten from a json
file and then converted to respective objects but all that is being done here"""
vehicles = [
    {"vehicle_id": "MRT01", "make": 'Toyota', "model": "V1", "year": "2020", "rental_rate": 2000, "availability": False, "type":'R'},
    {"vehicle_id": "MRT02", "make": 'Honda', "model": "V1", "year": "2021", "rental_rate": 2000, "availability": True, "type":'R'},
    {"vehicle_id": "MRT03", "make": 'Toyota', "model": "V1", "year": "2019", "rental_rate": 2000, "availability": False, "type":'R'},
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
    {"c_id": "C01", "name":"Rahul", "contact_info":"rahul@xyz.com", "rental_history":{"#1":["MRT01", 10], "#2":["MRT03", 15],}, 'c_type':'R', 'renting':True, 'loyalty_points':5, 'due_date':"1-12-2024"},
    {"c_id": "C02", "name":"Abhay", "contact_info":"abhay@xyz.com", "rental_history":{"#1":["MRT04", 40], "#2":["MRT01", 1]}, 'c_type':'R', 'renting':True, 'loyalty_points':59, 'due_date':"1-12-2024"},
    {"c_id": "C03", "name":"Rajesh", "contact_info":"rajesh@xyz.com", "rental_history":{"#1":["MRT09", 20], "#2":["MRT02", 105]}, 'c_type':'P', 'renting':False, 'loyalty_points':370, 'due_date':""},
]


rent = 0

class Vehicle:
    vehicle_type = 'Car'
    global rent
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

    def return_rent(self, rental_duration):
        rent = self.rental_rate * rental_duration
        return rent


class LuxuryVehicle(Vehicle):
    def __init__(self, vehicle_id, make, model, year, rental_rate, availability, extra_features):
        super().__init__(vehicle_id, make, model, year, rental_rate, availability)
        self.extra_features = extra_features
        self.rental_rate = rental_rate + rental_rate * 0.2


class Customer:

    def __init__(self, c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, due_date):
        self.c_id = c_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = rental_history
        self.renting = renting
        self.loyalty_points = loyalty_points
        self.c_type = c_type
        self.due_date = due_date
    def login(self):
        print("Welcome to MRT Rentals !")
        print("To login into your profile, enter your Customer ID and Name ")
        c_id = input("Customer ID: ")
        name = input("Name :")

        if c_id == self.c_id and name == self.name:
            if self.c_type == 'P':
                print("Welcome PREMIUM CUSTOMER")
            print("Login Successful")
            print("Here are your options:")
            print("1. View Customer details")
            print("2. View History")
            print("3. Rent a car")
            print("4. Return a car")
            print("")
            if self.renting:
                print("You currently have an active rental")
                for customer in customers:
                    if customer["c_id"] == self.c_id:
                        last_vehicle = list(customer["rental_history"])[-1]
                        print(customer["rental_history"][list([last_vehicle])[-1]])
                        print(f"Due date : {self.due_date}")
            print("")
            choice = input("What is your choice? : ")
            if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                self.query_handler(choice)
            else:
                print("Invalid Choice")
        else:
            print("Invalid Customer ID or Name")



    def print_customer(self):
        print(f"Hello dear customer ! ")
        print(f"Your Customer ID is : {self.c_id}")
        print(f"Your Name is : {self.name}")
        print(f"Your Contact Info is : {self.contact_info}")

    def view_history(self):
        print(f"Hello dear customer ! ")
        print(f"Your Customer ID is : {self.c_id}")
        print(f"Your Rental history is : {self.rental_history}")

    def rent(self, choice, duration):
        for car in cars:
            if car.vehicle_id == choice:
                car.rent_vehicle(self.c_id, duration)
                if self.c_type == 'P':
                    print("Do you want to avail the 10% discount exclusively for premium customers ?")
                    choice = input("y/n?: ")
                    if choice == 'y':
                        Rent = int(car.return_rent(duration))
                        print(Rent)
                        new_rent = Rent - 0.1 * Rent
                        print(f"Your Discounted Rental Rate is : {new_rent}")
                        print("Your vehicle has successfully been rented")



    def query_handler(self, choice):
        if choice == "1":
            print(f"Your Customer ID is : {self.c_id}")
            print(f"Your Name is : {self.name}")
            print(f"Your Contact Info is : {self.contact_info}")
        elif choice == "2":
            print(f"Your Rental history is : ")
            print(self.rental_history)
        elif choice == "3":
            print("The available vehicles are : ")
            for vehicle in vehicles:
                if vehicle["availability"]:
                    print(vehicle)
            print("Enter the Vehicle ID of the vehicle you want to rent and duration of the rent")
            choice = input("Vehicle ID : ")
            duration = input("Duration of the rent : ")
            self.rent(choice, int(duration))
            print(f"Your Loyalty points : {self.loyalty_points}")
            print("Structure for Point Benefits: ")
            print("For every 50 points, you can avail a 10% discount")
            print("For every 500 points, you can avail a free rental")
            if self.loyalty_points >= 50:
                print("You are eligible for a discount/free rental based on above tariff")
                print("Do you choose to avail it?")
                choice = input("y/n: ")
                if choice == "y":
                    if self.loyalty_points >= 500:
                        print("Discount or free rental ? ")
                        choice = input("1 for Discount and 2 for free rental: ")
                        if choice == "1":
                            self.loyalty_points -= 50
                            print("Congratulations!")
                            print("You are eligible for a 10% discount on your next visit")
                        else:
                            self.loyalty_points -= 500
                            print("Congratulations!")
                            print("You are eligible for a free rental on your next visit")
                    else:
                        self.loyalty_points -= 50
                        print("Congratulations!")
                        print("You are eligible for a 10% discount on your next visit")
                print("Thank you for choosing MRT Rentals.")
        elif choice == "4":
            print("The vehicle that you are renting now is : ")
            if self.renting:
                for customer in customers:
                    if customer["c_id"] == self.c_id:
                        last_vehicle = list(customer["rental_history"])[-1]
                        print(customer["rental_history"][last_vehicle])
                        print(f"{customer["rental_history"][last_vehicle][0]} has been successfully returned")
                        print("Thank you for using MRT Rentals !")
            else:
                print("You are currently not renting any vehicle")



class RegularCustomer(Customer):
    def __init__(self, c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, due_date):
        super().__init__(c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, due_date)



class PremiumCustomer(Customer):
    def __init__(self, c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, due_date):
        super().__init__(c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, due_date)



class RentalManager:
    def list_vehicles(self):
        print("List of available Rental Vehicles")
        for i in vehicles:
            if i["availability"]:
                print(f"{i['vehicle_id']} : {i['make']} : {i['model']}")

    def add_vehicle(self, vehicle_id, make, model, year, rental_rate, availability):
        vehicles.append({"vehicle_id": vehicle_id, "make": make, "model": model, "year": year, rental_rate: rental_rate, "availability": availability})
        print("Successsfully added")
        response = input("Would you like to view the updated vehicle list [y/n] ?")
        if response == "y":
            for vehicle in vehicles:
                print(f"{vehicle['vehicle_id']} : {vehicle['make']} : {vehicle['model']}")

    def remove_vehicle(self, vehicle_id):
        for vehicle in vehicles:
            if vehicle["vehicle_id"] == vehicle_id:
                vehicles.remove(vehicle)
        print("Successsfully removed")
        response = input("Would you like to view the updated vehicle list [y/n] ?")
        if response == "y":
            for vehicle in vehicles:
                print(f"{vehicle['vehicle_id']} : {vehicle['make']} : {vehicle['model']}")

    def generate_report(self):
        print(f"Vehicles In Use Report:")
        count = 0
        for vehicle in vehicles:
            if not(vehicle[("availability")]):
                count += 1
                print(f"{vehicle['vehicle_id']} : {vehicle['make']} : {vehicle['model']}")

        if count == 0:
            print("No Vehicles In Use")

        print("Customer report")
        for customer in customers:
            print(f"{customer['c_id']} : {customer['name']} : {customer['contact_info']}, {customer['rental_history']}")


cars = list()
people = list()
for vehicle in vehicles:
    if vehicle['type'] == 'R':
        cars.append(Vehicle(vehicle["vehicle_id"], vehicle["make"], vehicle["model"], vehicle["year"], vehicle["rental_rate"], vehicle["availability"]))
    else:
        cars.append(LuxuryVehicle(vehicle["vehicle_id"], vehicle["make"], vehicle["model"], vehicle["year"], vehicle["rental_rate"], vehicle["availability"], vehicle["extra_features"]))

for customer in customers:
    if customer['c_type'] == 'R':
        people.append(RegularCustomer(customer["c_id"], customer["name"], customer["contact_info"], customer["rental_history"], customer["renting"], customer["loyalty_points"], customer["c_type"], customer["due_date"]))
    else:
        people.append(PremiumCustomer(customer["c_id"], customer["name"], customer["contact_info"], customer["rental_history"], customer["renting"], customer["loyalty_points"], customer["c_type"], customer["due_date"]))


if __name__ == "__main__":


    people[1].login()



    #Manager = RentalManager()
    #Manager.list_vehicles()    # Working
    #Manager.generate_report()   # Working
   # Manager.add_vehicle('MRT20', 'Kia', 'V3', 2024, 7000, True) # Working
   # Manager.remove_vehicle('MRT20') # Working

