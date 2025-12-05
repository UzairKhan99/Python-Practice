You’re very close—just a few syntax and name fixes.
Here is a clean, correct version with explanation in comments that you can paste directly into your IDE:

```python
# ============================================
# Dictionary: keys(), values(), items()
# ============================================

# Correct dictionary:
# - Strings must be in quotes
# - Key and value are separated with :
# - Pairs are separated with commas

profile = {
    "name": "raju",
    "age": 99
}

print("Full dictionary:", profile)

# ---------------------------
# 1) keys()
# ---------------------------
# profile.keys() returns a "view" of all keys.

all_keys = profile.keys()
print("\nprofile.keys():", all_keys)          # dict_keys([...])
print("list(profile.keys()):", list(all_keys))  # convert to list if needed

# ---------------------------
# 2) values()
# ---------------------------
# profile.values() returns a "view" of all values.

all_values = profile.values()
print("\nprofile.values():", all_values)            # dict_values([...])
print("list(profile.values()):", list(all_values))  # convert to list

# ---------------------------
# 3) items()
# ---------------------------
# profile.items() returns (key, value) pairs.

all_items = profile.items()
print("\nprofile.items():", all_items)              # dict_items([...])
# list of (key, value) tuples
print("list(profile.items()):", list(all_items))

# Example of looping over items:
print("\nLooping over key–value pairs:")
for key, value in profile.items():
    print(key, "->", value)

# Quick summary (as comments):
# profile.keys()   -> all keys
# profile.values() -> all values
# profile.items()  -> all (key, value) pairs
# list(...)        -> convert the view to a real list if you need indexing, etc.
```
