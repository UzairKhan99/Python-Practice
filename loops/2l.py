# ====================================
# Dictionary basics + keys / values / items
# ====================================

# Empty dictionary
profile = {}

# A dictionary with some data (example)
profile = {
    "name": "Uzair",
    "age": 20,
    "city": "Lahore"
}

print("Full dictionary:")
print(profile)

print("\n=== 1) Loop over KEYS (3 ways) ===")

# Way 1: directly over the dictionary (common and simple)
for k in profile:
    print("Key:", k)

# Way 2: using keys() (same result, more explicit)
for k in profile.keys():
    print("Key from keys():", k)

# Way 3: get list of keys (if you need a list)
keys_list = list(profile.keys())
print("keys_list:", keys_list)


print("\n=== 2) Loop over VALUES ===")

for v in profile.values():
    print("Value:", v)

values_list = list(profile.values())
print("values_list:", values_list)


print("\n=== 3) Loop over ITEMS (key, value pairs) ===")

# items() gives (key, value) pairs
for k, v in profile.items():
    print("Key:", k, "-> Value:", v)

items_list = list(profile.items())
# e.g. [('name', 'Uzair'), ('age', 20), ('city', 'Lahore')]
print("items_list:", items_list)


print("\n=== 4) Using input with dictionary (optional demo) ===")

# You can add data to the dictionary from user input
user_profile = {}

user_profile["name"] = input("Enter your name: ")
user_profile["age"] = int(input("Enter your age: "))
user_profile["city"] = input("Enter your city: ")

print("\nUser profile dictionary:")
print(user_profile)

print("\nLooping through user_profile with items():")
for key, value in user_profile.items():
    print(key, ":", value)

# Quick summary (as comments):
# profile.keys()   -> all keys
# profile.values() -> all values
# profile.items()  -> (key, value) pairs
# for k in profile:        -> loops over keys
# for k, v in profile.items(): -> loops over keys and values together
