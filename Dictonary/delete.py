You are doing deletion correctly
just a couple of small fixes and explanations will help.
Here is a clean version you can copy–paste into your IDE:

```python
# ============================
# Deleting from a dictionary
# ============================

# Note: avoid extra spaces in keys like 'name '.
# Better to write "name" without space.

my_dict = {
    "name": "python",
    "version": 3.9
}

print("Original my_dict:", my_dict)

# -----------------------------
# 1) del my_dict['version']
# -----------------------------
# del removes the KEY and its VALUE from the dictionary.

del my_dict["version"]

print("After del my_dict['version']:", my_dict)
# Now my_dict has only: {"name": "python"}

# -----------------------------
# 2) Using pop() to delete and RETURN value
# -----------------------------

my_dict = {
    "name": "python",
    "version": 3.9
}

print("\nReset my_dict:", my_dict)

removed_value = my_dict.pop("version")   # removes 'version' and returns 3.9
print("Removed value from pop('version'):", removed_value)
print("After pop('version'):", my_dict)

# -----------------------------
# 3) Deleting whole dictionary
# -----------------------------
# WARNING: After this, you cannot use my_dict anymore.

del my_dict
# print(my_dict)   # This would give an error: NameError: name 'my_dict' is not defined

# Quick summary (as comments):
# del my_dict["key"]  -> remove that key–value pair.
# my_dict.pop("key")  -> remove the pair AND give you the value.
# del my_dict         -> delete the entire dictionary variable.
```
