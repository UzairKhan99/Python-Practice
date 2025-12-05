# ==============================
# 'in' and 'not in' in Python
# ==============================
#
# 'in'      -> checks if a value IS present in a sequence (list, string, etc.)
# 'not in'  -> checks if a value is NOT present in a sequence
#
# They return True or False (boolean).

lst_1 = [1, 2, 3, 4, 5]
print("Our list:", lst_1)

check = int(input("Enter the number you want to check = "))

# -------------------------
# Using 'in'
# -------------------------
if check in lst_1:
    print("Yes, it is present (checked with 'in')")
else:
    print("No, it is NOT present (checked with 'in')")

# -------------------------
# Using 'not in'
# -------------------------
# This is the same logic written using 'not in'
if check not in lst_1:
    print("Confirmed using 'not in': the number is NOT in the list")
else:
    print("Confirmed using 'not in': the number IS in the list")

# -------------------------
# Extra small examples
# -------------------------

# Example with strings
name = "python"
print("\nString example with 'in' and 'not in':")
print("'p' in name  ->", 'p' in name)       # True
print("'z' in name  ->", 'z' in name)       # False
print("'z' not in name ->", 'z' not in name)  # True

# Quick summary (as comments):
# value in sequence     -> True if value exists inside sequence
# value not in sequence -> True if value does NOT exist inside sequence
