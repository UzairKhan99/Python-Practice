You’re talking about ** Python dictionaries**. Let me put your notes into a clean explanation + code that you can paste into your IDE.

```python
# ============================================
# PYTHON DICTIONARY – BASIC CONCEPTS
# ============================================
#
# In a dictionary we store data in **pairs**:
#   key : value
#
# Example idea:
#   "apple" : "a red or green fruit"
#
# General syntax:
#   my_dict = {
#       key1: value1,
#       key2: value2,
#   }
#
# PROPERTIES:
# 1) Key–value pairs, separated by commas
# 2) Ordered (in modern Python: keeps insertion order)
# 3) Mutable (you can add / change / delete entries)
# 4) Dynamic & Heterogeneous
#    - Can grow/shrink
#    - Keys and values can be of different data types


print("=== 1) CREATING A DICTIONARY (KEY–VALUE PAIRS) ===")

# Example: word dictionary
meaning_dict = {
    "apple": "a red or green fruit",
    "banana": "a long yellow fruit",
    "python": "a programming language",
}

print("meaning_dict:", meaning_dict)
print("Value for key 'apple':", meaning_dict["apple"])   # key -> value
print("Value for key 'python':", meaning_dict["python"])


print("\n=== 2) PROPERTIES EXPLAINED ===")

# 1) Key–value pairs, commas between pairs
example = {
    "name": "Sagar",   # key: "name", value: "Sagar"
    "age": 100,        # key: "age",  value: 100
    "marks": 50.5,     # key: "marks", value: 50.5
}
print("example:", example)

# 2) Ordered → preserves insertion order (Python 3.7+)
print("Keys in order:", list(example.keys()))

# 3) Mutable → you can change values
example["age"] = 101
print("After updating age:", example)

# 4) Dynamic & Heterogeneous:
#    - You can add new keys anytime
#    - Values can be int, float, list, dict, etc.
example["subjects"] = ["Math", "English", "Science"]  # list as a value
example["details"] = {"city": "Lahore",
                      "country": "Pakistan"}  # dict as a value

print("After adding new keys:", example)


print("\n=== 3) ADDING AND UPDATING ELEMENTS ===")

person = {
    "name": "Python",
    "version": 3.9
}
print("Original person:", person)

# Add new key
person["author"] = "Guido van Rossum"
print("After adding 'author':", person)

# Update existing key
person["version"] = 4.0
print("After updating 'version' to 4.0:", person)

# Using update() to add/update multiple keys
person.update({
    "typed": True,
    "year": 1991
})
print("After person.update({...}):", person)


print("\n=== 4) DELETING ELEMENTS ===")

my_dict = {
    "name": "Python",
    "version": 3.9,
    "release": 2024,
}
print("Original my_dict:", my_dict)

# Delete a single key–value pair
del my_dict["version"]
print("After del my_dict['version']:", my_dict)

# pop() → deletes and returns value
removed = my_dict.pop("release")
print("Removed value from pop('release'):", removed)
print("After pop('release'):", my_dict)


print("\n=== 5) LOOPING OVER A DICTIONARY ===")

languages = {
    "py": "Python",
    "js": "JavaScript",
    "cpp": "C++",
}

print("languages:", languages)

print("\nKeys:")
for k in languages.keys():
    print(k)

print("\nValues:")
for v in languages.values():
    print(v)

print("\nKey–value pairs (items):")
for k, v in languages.items():
    print(k, "->", v)


# Quick summary (as comments):
# - Dictionary = collection of key: value pairs.
# - 1 pair = key : value (separated by commas between pairs).
# - Ordered, mutable, dynamic, heterogeneous.
# - Keys must be unique; values can repeat.
# - Access: my_dict[key]
# - Add / update: my_dict[key] = value
# - Delete: del my_dict[key] or my_dict.pop(key)
```
