You’re very close—just a few syntax fixes and an explanation of `get()`.
Here is a clean, corrected version you can copy–paste into your IDE:

```python
# =====================================
# Dictionary .get() – safe key access
# =====================================

# Correct dictionary syntax:
# - Put a comma between pairs
# - Make sure strings are properly quoted

profile = {
    "name": "Raju",
    "age": 100
}

print("profile:", profile)

# -----------------------------
# Accessing normally ([])
# -----------------------------
# This works if the key exists. If it does NOT exist, it raises an error.

age_normal = profile["age"]   # works, because "age" is present
print("Age using []:", age_normal)

# The following (if uncommented) would give a KeyError, because "city" is not in the dictionary:
# city_normal = profile["city"]


# -----------------------------
# Using get() method
# -----------------------------
# profile.get("age") returns the value if the key exists,
# otherwise it returns None (or a default value if you provide one).

age = profile.get("age")
print("Age using get('age'):", age)   # 100

# If the key does not exist, get() returns None by default:
city = profile.get("city")
print("City using get('city'):", city)   # None


# You can also provide a DEFAULT value:
city_with_default = profile.get("city", "Not specified")
print("City using get('city', 'Not specified'):", city_with_default)


# Quick summary (as comments):
# profile["age"]          -> direct access; error if key missing.
# profile.get("age")      -> safe access; returns None if missing.
# profile.get("age", 0)   -> safe access; returns 0 (or any default) if missing.
```
