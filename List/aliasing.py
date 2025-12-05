# ============================================
# Aliasing vs Not Aliasing (Copy) in Python
# ============================================
#
# Aliasing:
#   - Two variables point to the SAME list in memory.
#   - Changing the list using one variable also changes it for the other.
#
# Not Aliasing (Copy):
#   - We create a NEW, SEPARATE list.
#   - Changing one list does NOT affect the other.

# ------------------------
# Example 1: ALIASING
# ------------------------
print("=== ALIASING EXAMPLE ===")

list_1 = [1, 2, 3]   # original list
list_2 = list_1      # aliasing: list_2 points to the SAME list as list_1

print("Before change:")
print("list_1:", list_1)
print("list_2:", list_2)

# Change through list_2
list_2[0] = 100

print("\nAfter doing list_2[0] = 100:")
print("list_1:", list_1)  # will also show 100 at index 0
print("list_2:", list_2)

# Show that both variables point to the same object in memory
print("\nIDs in memory (same means aliasing):")
print("id(list_1):", id(list_1))
print("id(list_2):", id(list_2))

# Explanation:
# list_1 and list_2 have the SAME id, so they are two names for one list.
# That is called ALIASING.


# -----------------------------
# Example 2: NOT ALIASING (COPY)
# -----------------------------
print("\n\n=== NOT ALIASING (COPY) EXAMPLE ===")

list_3 = [8, 7, 4, 1]     # original list
list_4 = list_3.copy()    # make a NEW list (shallow copy)

print("Before change:")
print("list_3:", list_3)
print("list_4:", list_4)

# Change through list_4
list_4[0] = 999

print("\nAfter doing list_4[0] = 999:")
print("list_3:", list_3)  # stays the same
print("list_4:", list_4)  # only this one changes

# Show that they are different objects in memory
print("\nIDs in memory (different means no aliasing):")
print("id(list_3):", id(list_3))
print("id(list_4):", id(list_4))

# Explanation:
# list_3 and list_4 have DIFFERENT ids, so they are two separate lists.
# Changing list_4 does NOT affect list_3.
