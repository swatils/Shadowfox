#1.VARIABLES
#1.1 datatype
pi = 22 / 7
pi_type = type(pi)
print("pi =", pi)
print("Type of pi =", pi_type)

#1.2
# This will throw a SyntaxError because 'for' is a reserved keyword in Python.
# for = 4
print("'for' cannot be used as a variable name because it's a reserved keyword used for loops.")

#1.3
P = 10000  
R = 5  
T = 3  
simple_interest = (P * R * T) / 100
print("Simple Interest for 3 years =", simple_interest)

#2. NUMBERS
#2.1
def format_example(num, char):
    formatted = "{0:{1}}".format(num, char)
    return formatted

result = format_example(145, 'o')
print("Formatted result:", result)
print("Note: 'o' is not a standard format specifier, so the result is unusual.")

#2.2
radius = 84  # in meters
pi = 3.14
water_per_sqm = 1.4  # liters

area = pi * radius ** 2
total_water = int(area * water_per_sqm)  # convert to int to remove decimal

print("Total amount of water in the pond (liters):", total_water)

#2.3
distance = 490  # in meters
time = 7 * 60   # convert 7 minutes to seconds

speed = int(distance / time)
print("Speed in meters/second:", speed)

#3 LIST
# Initial Justice League members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial list:", justice_league)

# 1. Calculate the number of members
print("1. Number of members in Justice League:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("2. After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning (make her leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("3. After making Wonder Woman the leader:", justice_league)

# 4. Separate Aquaman and Flash by inserting "Green Lantern" between them
# Find index of Aquaman and Flash
index_aqua = justice_league.index("Aquaman")
index_flash = justice_league.index("Flash")
# Ensure Aquaman comes before Flash
if index_aqua > index_flash:
    index_aqua, index_flash = index_flash, index_aqua

# Remove original Green Lantern before re-inserting
justice_league.remove("Green Lantern")
justice_league.insert(index_flash, "Green Lantern")
print("4. After separating Aquaman and Flash with Green Lantern:", justice_league)

# 5. Replace the team with a new list
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("5. New Justice League team:", justice_league)

# 6. Sort the list alphabetically
justice_league.sort()
print("6. Sorted Justice League:", justice_league)

# BONUS: New leader is at index 0
print("BONUS: The new leader is:", justice_league[0])

#6. DICTIONARY

# Task 6.1: List of friends with name length
friends = ['Aditya', 'Riya', 'Kunal', 'Meera', 'Sanjay']
friend_tuples = [(name, len(name)) for name in friends]
print("Friend Tuples (Name, Length):")
print(friend_tuples)

# Task 6.2: Expense tracking
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print(f"\nYour total expenses: ₹{your_total}")
print(f"Partner's total expenses: ₹{partner_total}")

# Who spent more
if your_total > partner_total:
    print("You spent more than your partner.")
elif partner_total > your_total:
    print("Your partner spent more than you.")
else:
    print("Both spent the same amount.")

# Category with maximum difference
max_diff = 0
diff_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_diff:
        max_diff = difference
        diff_category = category

print(f"\nCategory with maximum difference: {diff_category}")
print(f"Difference: ₹{max_diff}")

#9. INHERITANCE

# Base Class
class MobilePhone:
    def _init_(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, name):
        print(f"Incoming call from {name}")

    def take_picture(self):
        print(f"Taking picture with {self.rear_camera} rear camera.")

    def phone_info(self):
        print("----- Phone Info -----")
        print(f"Screen Type: {self.screen_type}")
        print(f"Network Type: {self.network_type}")
        print(f"Dual SIM: {self.dual_sim}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")
        print("----------------------\n")


# Apple class inheriting from MobilePhone
class Apple(MobilePhone):
    def _init_(self, front_camera, rear_camera, ram, storage):
        super()._init_("Touch Screen", "5G", False, front_camera, rear_camera, ram, storage)
        self.brand = "Apple"

# Samsung class inheriting from MobilePhone
class Samsung(MobilePhone):
    def _init_(self, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super()._init_("Touch Screen", network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.brand = "Samsung"


# Creating Apple objects
iphone_13 = Apple("12MP", "48MP", "4GB", "64GB")
iphone_13.phone_info()
iphone_13.make_call("9999999999")

iphone_se = Apple("7MP", "12MP", "2GB", "32GB")
iphone_se.phone_info()
iphone_se.take_picture()

# Creating Samsung objects
samsung_s22 = Samsung("5G", True, "16MP", "32MP", "4GB", "64GB")
samsung_s22.phone_info()
samsung_s22.receive_call("Mom")

samsung_m30 = Samsung("4G", True, "8MP", "16MP", "3GB", "32GB")
samsung_m30.phone_info()
samsung_m30.take_picture()
