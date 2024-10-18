"""Code for the first assignment of the software subsystem of MRT. Python Tutorial. Aim: To get used to object-oriented programming and use of objects and classes.
The goal is to make a working interface for a customer and manager of a rental service"""

# Importing packages
from datetime import datetime, date
import datetime
from multipledispatch import dispatch
from dateutil.relativedelta import relativedelta
import time

# Data of vehicles of the rental service
vehicles = [
    {"vehicle_id": "MRT01", "make": 'Toyota', "model": "V1", "year": "2020", "rental_rate": 2000, "availability": False,
     "type": 'R'},
    {"vehicle_id": "MRT02", "make": 'Honda', "model": "V1", "year": "2021", "rental_rate": 2000, "availability": True,
     "type": 'R'},
    {"vehicle_id": "MRT03", "make": 'Toyota', "model": "V1", "year": "2019", "rental_rate": 2000, "availability": False,
     "type": 'R'},
    {"vehicle_id": "MRT04", "make": 'Hyundai', "model": "V1", "year": "2014", "rental_rate": 1500,
     "availability": True, "type": 'R'},
    {"vehicle_id": "MRT05", "make": 'Kia', "model": "V1", "year": "2022", "rental_rate": 3000, "availability": True,
     "type": 'R'},
    {"vehicle_id": "MRT06", "make": 'Toyota', "model": "V2", "year": "2021", "rental_rate": 2500, "availability": True,
     "type": 'R'},
    {"vehicle_id": "MRT07", "make": 'Maruti', "model": "V1", "year": "2018", "rental_rate": 1000, "availability": True,
     "type": 'R'},
    {"vehicle_id": "MRT08", "make": 'Mercedes', "model": "V1", "year": "2021", "rental_rate": 5000,
     "availability": True, "type": 'L', "extra_features": 'GPS'},
    {"vehicle_id": "MRT09", "make": 'Mercedes', "model": "V2", "year": "2022", "rental_rate": 7000,
     "availability": True, "type": 'L', "extra_features": 'GPS'},
    {"vehicle_id": "MRT10", "make": 'Audi', "model": "V1", "year": "2023", "rental_rate": 10000, "availability": True,
     "type": 'L', "extra_features": 'Stereo System'},
]

# Data of customers of the rental service

customers = [
    {"c_id": "C01", "name": "Rahul", "contact_info": "rahul@xyz.com",
     "rental_history": {"#1": ["MRT01", 10], "#2": ["MRT03", 15], }, 'c_type': 'R', 'renting': True,
     'loyalty_points': 5, 'date_rented': datetime.date(2024, 10, 12)},
    {"c_id": "C02", "name": "Abhay", "contact_info": "abhay@xyz.com",
     "rental_history": {"#1": ["MRT04", 40], "#2": ["MRT01", 100]}, 'c_type': 'R', 'renting': True, 'loyalty_points': 59,
     'date_rented': datetime.date(2024, 10, 14)},
    {"c_id": "C03", "name": "Rajesh", "contact_info": "rajesh@xyz.com",
     "rental_history": {"#1": ["MRT09", 20], "#2": ["MRT02", 105]}, 'c_type': 'P', 'renting': False,
     'loyalty_points': 370, 'date_rented': ""},
    {"c_id": "C04", "name": "Kunal", "contact_info": "rahul@xyz.com",
     "rental_history": {"#1": ["MRT06", 140], "#2": ["MRT08", 15], }, 'c_type': 'R', 'renting': False,
     'loyalty_points': 5, 'date_rented': date.today()},
]


# Vehicle class with class attribute vehicle_type = 'Car' and instance attributes for Vehicleid, Makke, Model, Year, Rental rate, Availability
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

    # Function to print the details of a vehicle
    def print_vehicle(self):
        print(f"Your vehicle is : {self.vehicle_id}")
        print(f"Its Make is : {self.make}")
        print(f"Its Model is : {self.model}")
        print(f"Its Year of manufacture is : {self.year}")
        print(f"Its Rental Rate is : {self.rental_rate}")
        print(f"Its Availability is : {self.availability}")

    # Function to return the rent of a vehicle
    def rent_vehicle(self, rental_duration):
        rent = self.rental_rate * rental_duration
        return rent

    # Function to return required vehicle to the rental service
    def return_vehicle(self):
        self.availability = True
        print(f"Your vehicle has been successfully returned.")
        print(f"Thank you for choosing MRT Rentals.")


# Child class of vehicle with extra features and higher rental rate
class LuxuryVehicle(Vehicle):
    def __init__(self, vehicle_id, make, model, year, rental_rate, availability, extra_features):
        super().__init__(vehicle_id, make, model, year, rental_rate, availability)
        self.extra_features = extra_features
        self.rental_rate = rental_rate + rental_rate * 0.2


# Class of customers with instance variables for Customer ID, Name, Contact Info, Rental History, Renting status, Loyalty points, Type, Date rented
class Customer:

    def __init__(self, c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, date_rented):
        self.c_id = c_id
        self.name = name
        self.contact_info = contact_info
        self.rental_history = rental_history
        self.renting = renting
        self.loyalty_points = loyalty_points
        self.c_type = c_type
        self.date_rented = date_rented
        self.last_rent = int(list(self.rental_history.keys())[-1][-1])

    # Print the contact info, CID and Name of the customer
    def print_customer(self):
        print(f"Hello dear customer ! ")
        print(f"Your Customer ID is : {self.c_id}")
        print(f"Your Name is : {self.name}")
        print(f"Your Contact Info is : {self.contact_info}")

    # View the Rental history of the customer
    def view_history(self):
        print(f"Hello dear customer ! ")
        print(f"Your Customer ID is : {self.c_id}")
        print(f"Your Rental history is : {self.rental_history}")

    # Function to handle the queries of the customer from the login function
    def query_handler(self, choice):
        if choice == "1":
            print(f"Your Customer ID is : {self.c_id}")
            print(f"Your Name is : {self.name}")
            print(f"Your Contact Info is : {self.contact_info}")
            login(self.c_id)
        elif choice == "2":
            print(f"Your Rental history is : ")
            print(self.rental_history)
            login(self.c_id)
        elif choice == "3":
            if self.renting:
                print("Please return your vehicle before renting again.")
                time.sleep(1)
                login(self.c_id)

            else:
                print("The available vehicles are : ")
                for vehicle in vehicles:
                    if vehicle["availability"]:
                        if vehicle["type"] == "R":
                            print(
                                f"Vehicle ID: {vehicle["vehicle_id"]}, Make : {vehicle['make']}, Model : {vehicle['model']}, Year : {vehicle['year']}, Rental rate : {vehicle['rental_rate']}")
                        else:
                            print(
                                f"Vehicle ID: {vehicle["vehicle_id"]}, Make : {vehicle['make']}, Model : {vehicle['model']}, Year : {vehicle['year']}, Rental rate : {vehicle['rental_rate']}, Luxury Feature: {vehicle['extra_features']}")
                print("Do you want to apply any search filters?")
                yn = input("y/n? : ")
                if yn == "y":
                    print("The following are the search filters : ")
                    print("1. Rental Rate")
                    print("2. Luxury Feature")
                    print("3. Make")
                    print("4. Year")
                    print("5. Model")
                    choice = input("Enter your choice : ")
                    self.filter(choice)
                    print("Enter the Vehicle ID of the vehicle you want to rent and duration of the rent")
                    choice = input("Vehicle ID : ")
                    duration = input("Duration of the rent : ")
                    if self.c_type == 'P':
                        self.premium_rent(choice, int(duration))
                    self.renting = True
                    print(f"Your Loyalty points : {self.loyalty_points}")
                    print("Structure for Point Benefits: ")
                    time.sleep(0.7)
                    print("For every 50 points, you can avail a 10% discount")
                    time.sleep(0.7)
                    print("For every 500 points, you can avail a free rental")
                    time.sleep(0.7)
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
                    self.rental_history.update({f'#{self.last_rent + 1}': [choice, int(duration)]})
                    print("Thank you for choosing MRT Rentals.")
                    login(self.c_id)
                else:
                    print("Enter the Vehicle ID of the vehicle you want to rent and duration of the rent")
                    choice = input("Vehicle ID : ")
                    duration = input("Duration of the rent : ")
                    if self.c_type == 'P':
                        self.premium_rent(choice, int(duration))
                    self.renting = True
                    time.sleep(1)
                    print(f"Your Loyalty points : {self.loyalty_points}")
                    print("Structure for Point Benefits: ")
                    time.sleep(0.5)
                    print("For every 50 points, you can avail a 10% discount")
                    time.sleep(0.5)
                    print("For every 500 points, you can avail a free rental")
                    time.sleep(0.5)
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
                    self.rental_history.update({f'#{self.last_rent + 1}': [choice, int(duration)]})
                    self.date_rented = date.today()
                    self.loyalty_points += 100
                    print("Thank you for choosing MRT Rentals.")
                    login(self.c_id)
        elif choice == "4":
            print("The vehicle that you are renting now is : ")
            if self.renting:
                self.renting = False
                for customer in customers:
                    if customer["c_id"] == self.c_id:
                        last_vehicle = list(customer["rental_history"])[-1]
                        print(customer["rental_history"][list([last_vehicle])[-1]][0])
                        print(
                            f"{customer["rental_history"][list([last_vehicle])[-1]][0]} has been successfully returned")
                        print("Thank you for using MRT Rentals !")
                        login(self.c_id)
            else:
                print("You are currently not renting any vehicle")
                login(self.c_id)
        elif choice == "5":
            self.reservation()

    # Function to make reservations
    def reservation(self):
        print("Here is a list of cars and dates of availability: ")
        count = 1
        for car in cars:
            if car.availability:
                print(f"{count}. {car.vehicle_id}")
                count += 1
        print("Here is a list of cars that will be available later")
        count = 1
        for person in people:
            if person.renting:
                last_vehicle = list(person.rental_history)[-1]
                print(f"{count}.{person.rental_history[list([last_vehicle])[-1]][0]}")
                count += 1
                delta = relativedelta(days=+person.rental_history[list([last_vehicle])[-1]][-1])
                print(f"Due date : {person.date_rented + delta}")
        choice = input("Choose a vehicle to rent (Enter its vehicle ID) : ")
        time_str = input("Enter time in this format yyyy-mm-dd : ")
        date = datetime.datetime.strptime(time_str, "%Y-%m-%d")

        for car in cars:
            if car.vehicle_id == choice:
                if car.availability:
                    print(f"{car.vehicle_id} has been successfully reserved")
                    print("Thank you for using MRT Rentals !")
                    car.availability = False
                    login(self.c_id)
                else:
                    for person in people:
                        if person.renting:
                            last_vehicle = list(person.rental_history)[-1]
                            if person.rental_history[list([last_vehicle])[-1]][0] == choice:
                                delta = relativedelta(days=+person.rental_history[list([last_vehicle])[-1]][-1])
                                due_date = person.date_rented + delta
                                if due_date > date.date():
                                    print(f"Your choice {choice} is not available at the date that you have chosen")
                                    print("Please choose another date")
                                    time.sleep(1)
                                    self.reservation()
                                else:
                                    print(f"{car.vehicle_id} has been successfully reserved")
                                    print("Thank you for using MRT Rentals !")
                                    login(self.c_id)

    # Self explanatory
    def rent(self):
        print("Enter the Vehicle ID of the vehicle you want to rent and duration of the rent")
        choice = input("Vehicle ID : ")
        duration = input("Duration of the rent : ")
        if self.c_type == 'P':
            self.premium_rent(choice, int(duration))
        self.renting = True
        time.sleep(1)
        print(f"Your Loyalty points : {self.loyalty_points}")
        print("Structure for Point Benefits: ")
        time.sleep(0.5)
        print("For every 50 points, you can avail a 10% discount")
        time.sleep(0.5)
        print("For every 500 points, you can avail a free rental")
        time.sleep(0.5)
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
        self.rental_history.update({f'#{self.last_rent + 1}': [choice, duration]})
        print("Thank you for choosing MRT Rentals.")
        login(self.c_id)

    def filter(self, choice):
        count = 0
        if choice == "1":
            print("Input minimum and maximum: ")
            minimum = input("Minimum: ")
            maximum = input("Maximum: ")
            for car in cars:
                if int(minimum) <= car.rental_rate <= int(maximum):
                    if not (type(car) == LuxuryVehicle):
                        print(
                            f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}")
                        count += 1
                    else:
                        count += 1
                        print(
                            f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}, Luxury Feature: {car.extra_features}")
        elif choice == "2":
            print("The following are available luxury features: ")
            print("1. GPS")
            print("2. Stereo System")
            feature = ""
            ip = input("Choose a luxury feature: ")
            if ip == '1':
                feature = "GPS"
            elif ip == '2':
                feature = "Stereo System"
            else:
                print("Invalid Choice")
                print("Try again")
                self.filter(choice)
            for car in cars:
                if car.availability:
                    if type(car) == LuxuryVehicle:
                        if car.extra_features == feature:
                            count += 1
                            print(
                                f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}, Luxury Feature: {car.extra_features}")
        elif choice == "3":
            print("The following are available makes of our vehicles: ")
            print("1. Toyota")
            print("2. Honda")
            print("3. Hyundai")
            print("4. Mercedes")
            print("5. Kia")
            print("6. Maruti")
            print("7. Audi")
            inp = input("Choose a make: ")
            make = ""
            if inp == '1':
                make = 'Toyota'
            elif inp == '2':
                make = 'Honda'
            elif inp == '3':
                make = 'Hyundai'
            elif inp == '4':
                make = 'Mercedes'
            elif inp == '5':
                make = 'Kia'
            elif inp == '6':
                make = 'Maruti'
            elif inp == '7':
                make = 'Audi'
            for car in cars:
                if car.make == make:
                    if not (type(car) == LuxuryVehicle):
                        count += 1
                        print(
                            f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}")
                    else:
                        count += 1
                        print(
                            f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}, Luxury Feature: {car.extra_features}")
            if not (inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6' or inp == '7'):
                print("Invalid Choice")
                print("Try again")
                self.filter(choice)
        elif choice == "4":
            print("The following are available years of our vehicles: ")
            print("1. 2014")
            print("2. 2018")
            print("3. 2019")
            print("4. 2020")
            print("5. 2021")
            print("6. 2022")
            print("7. 2023")
            year = ""
            inp = input("Choose a year: ")
            if inp == '1':
                year = '2014'
            elif inp == '2':
                year = '2018'
            elif inp == '3':
                year = '2019'
            elif inp == '4':
                year = '2020'
            elif inp == '5':
                year = '2021'
            elif inp == '6':
                year = '2022'
            elif inp == '7':
                year = '2023'
            for car in cars:
                if car.year == year:
                    if not (type(car) == LuxuryVehicle):
                        count += 1
                        print(
                            f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}")
                    else:
                        count += 1
                        print(
                            f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}, Luxury Feature: {car.extra_features}")
            if not (inp == '1' or inp == '2' or inp == '3' or inp == '4' or inp == '5' or inp == '6' or inp == '7'):
                print("Invalid Choice")
                print("Try again")
                self.filter(choice)
        elif choice == "5":
            print("The following are available models of our vehicles: ")
            print("1. V1")
            print("2. V2")
            model = ''
            inp = input("Choose a model: ")
            if inp == '1':
                model = "V1"
            elif inp == '2':
                model = "V2"
            for car in cars:
                if car.model == model:
                    if not (type(car) == LuxuryVehicle):
                        count += 1
                        print(
                            f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}")
                    else:
                        count += 1
                        print(
                            f"Vehicle ID: {car.vehicle_id}, Make : {car.make}, Model : {car.model}, Year : {car.year}, Rental rate : {car.rental_rate}, Luxury Feature: {car.extra_features}")
            if not (inp == '1' or inp == '2'):
                print("Invalid Choice")
                print("Try again")
                self.filter(choice)
        if count == 0:
            print("No available vehicles for your search filters")
            print("Try again")
            self.filter(choice)


class RegularCustomer(Customer):
    def __init__(self, c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, date_rented):
        super().__init__(c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, date_rented)

    def rent(self, choice, duration):
        for car in cars:
            if car.vehicle_id == choice:
                self.availability = False
                rent = car.rent_vehicle(duration)
                print(f"Dear Customer, Thank you for choosing MRT Rentals.")
                print(f"Your Rental Rate is : {rent}")
                print(f"Your Customer ID is : {self.c_id}")


class PremiumCustomer(Customer):
    def __init__(self, c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, date_rented):
        super().__init__(c_id, name, contact_info, rental_history, renting, loyalty_points, c_type, date_rented)

    def premium_rent(self, choice, duration):
        for car in cars:
            if car.vehicle_id == choice:
                self.availability = False
                rent = car.rent_vehicle(duration)
                rent = rent - 0.1 * rent
                print(f"Dear Customer, Thank you for choosing MRT Rentals.")
                print(f"Your Discounted Rental Rate is : {rent}")
                print(f"Original Rate was: {rent / 0.9}")
                print(f"Your Customer ID is : {self.c_id}")


class RentalManager:

    def console(self):
        print("MRT Rental Manager Master Console")
        print("1. Generate list of available vehicles")
        print("2. Generate report of vehicles in use and customer report")
        print("3. Add a new vehicle to the fleet")
        print("4. Remove a vehicle from the fleet")
        print("5. Press Q to exit")
        choice = input("Choose an option: ")
        if choice == "1":
            self.list_vehicles()
            time.sleep(1)
            self.console()
        elif choice == "2":
            self.generate_report()
            time.sleep(1)
            self.console()
        elif choice == "3":
            print("Enter the specifications of the new vehicle: ")
            vehicle_id = input("Vehicle ID: ")
            make = input("Make: ")
            model = input("Model: ")
            year = input("Year: ")
            rental_rate = input("Rental Rate: ")
            self.add_vehicle(vehicle_id, make, model, year, rental_rate)
            time.sleep(1)
            self.console()
        elif choice == "4":
            self.list_vehicles()
            print("Enter the Vehicle ID  of the vehicle to be removed: ")
            vehicle_id = input("Vehicle ID: ")
            self.remove_vehicle(vehicle_id)
            time.sleep(1)
            self.console()
        elif choice == "Q":
            exit()
        else:
            print("Invalid Choice")
            print("Try again")
            time.sleep(1)
            self.console()

    def list_vehicles(self):
        print("List of available Rental Vehicles")
        for i in vehicles:
            if i["availability"]:
                print(f"{i['vehicle_id']} : {i['make']} : {i['model']}")

    def add_vehicle(self, vehicle_id, make, model, year, rental_rate):
        vehicles.append({"vehicle_id": vehicle_id, "make": make, "model": model, "year": year, rental_rate: rental_rate,
                         "availability": True})
        print("Successfully added")
        response = input("Would you like to view the updated vehicle list [y/n] ?")
        if response == "y":
            for vehicle in vehicles:
                print(f"{vehicle['vehicle_id']} : {vehicle['make']} : {vehicle['model']}")

    def remove_vehicle(self, vehicle_id):
        for vehicle in vehicles:
            if vehicle["vehicle_id"] == vehicle_id:
                vehicles.remove(vehicle)
        print("Successfully removed")
        response = input("Would you like to view the updated vehicle list [y/n] ?")
        if response == "y":
            for vehicle in vehicles:
                print(f"{vehicle['vehicle_id']} : {vehicle['make']} : {vehicle['model']}")

    def generate_report(self):
        print(f"Vehicles In Use Report:")
        count = 0
        for vehicle in vehicles:
            if not (vehicle[("availability")]):
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
        cars.append(
            Vehicle(vehicle["vehicle_id"], vehicle["make"], vehicle["model"], vehicle["year"], vehicle["rental_rate"],
                    vehicle["availability"]))
    else:
        cars.append(LuxuryVehicle(vehicle["vehicle_id"], vehicle["make"], vehicle["model"], vehicle["year"],
                                  vehicle["rental_rate"], vehicle["availability"], vehicle["extra_features"]))

for customer in customers:
    if customer['c_type'] == 'R':
        people.append(
            RegularCustomer(customer["c_id"], customer["name"], customer["contact_info"], customer["rental_history"],
                            customer["renting"], customer["loyalty_points"], customer["c_type"],
                            customer["date_rented"]))
    else:
        people.append(
            PremiumCustomer(customer["c_id"], customer["name"], customer["contact_info"], customer["rental_history"],
                            customer["renting"], customer["loyalty_points"], customer["c_type"],
                            customer["date_rented"]))


@dispatch()
def login():
    print("Welcome to MRT Rentals !")
    print("To login into your profile, enter your Customer ID and Name ")
    c_id = input("Customer ID: ")
    name = input("Name :")
    count = 0
    for self in people:
        if c_id == self.c_id and name == self.name:
            print("Login Successful")
            login(self.c_id)
        else:
            count += 1
            if count >= 4:
                print("Invalid Customer ID or Name")
                time.sleep(1)
                print("Please try again")
                time.sleep(1)
                login()


@dispatch(str)
def login(c_id):
    time.sleep(1.5)
    for person in people:
        if c_id == person.c_id:
            self = person
    if self.c_type == 'P':
        print("Welcome PREMIUM CUSTOMER")
    print("Here are your options:")
    print("1. View Customer details")
    print("2. View History")
    print("3. Rent a car")
    print("4. Return a car")
    print("5. Reserve a car")
    print("Q to Quit")
    print("")

    if self.renting:
        print("You currently have an active rental")
        for customer in customers:
            if customer["c_id"] == self.c_id:
                last_vehicle = list(customer["rental_history"])[-1]
                print(customer["rental_history"][list([last_vehicle])[-1]][0])
                delta = relativedelta(days=+customer["rental_history"][list([last_vehicle])[-1]][-1])
                print(f"Due date : {self.date_rented + delta}")
                print(f"Days remaining : {self.date_rented + delta - date.today()}")
    print("")
    choice = input("What is your choice? : ")
    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == '5':
        self.query_handler(choice)
    elif choice == "Q":
        print("Thank you for using MRT Rentals !")
        exit()


if __name__ == "__main__":
    # Console to choose customer or manager mode
    choice = input("Enter 1. for Customer login and 2. for Manager mode \n")
    if choice == '1':
        login()
    elif choice == '2':
        Manager = RentalManager()
        Manager.console()
