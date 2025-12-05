# ==============================
# 'in' with a list of strings
# ==============================

vegetagble = ["kerela", "Aloo", "Tamatar"]

print("List:", vegetagble)

# 'in' checks if the value is present in the list.
print('"kerela" in vegetagble ->', "kerela" in vegetagble)   # True

# Some extra checks:
print('"Aloo" in vegetagble   ->', "Aloo" in vegetagble)     # True
print('"Gobhi" in vegetagble  ->', "Gobhi" in vegetagble)    # False

# Note:
# - 'in' is case-sensitive:
# False, because "Aloo" has capital A
print('"aloo" in vegetagble   ->', "aloo" in vegetagble)

# Quick summary (as comments):
# value in list      -> True if value exists in the list, otherwise False.
# value not in list  -> True if value does NOT exist in the list.
