# =========================
# Python LIST – Basic Notes
# =========================

# 1) LIST is ORDERED
#    - Items keep the same order as you write them.
# 2) LIST is MUTABLE
#    - You can change, add, and remove items after creating it.
# 3) LIST is DYNAMIC
#    - Size can grow or shrink while the program runs.
# 4) LIST is HETEROGENEOUS
#    - It can store different data types together
#      (int, float, string, bool, etc.).

# -----------------------------------
# Creating a list (heterogeneous list)
# -----------------------------------
my_list = [1, 2, 3, 4, "hello", True]

# Print the whole list
print("my_list =", my_list)

# -----------------------------------
# ORDERED: access by index (position)
# Indexes: 0    1   2   3    4        5
# Values:  1    2   3   4   "hello"  True
# -----------------------------------
print("First item  (index 0):", my_list[0])   # 1
print("Fifth item  (index 4):", my_list[4])   # "hello"
print("Last item   (index 5):", my_list[5])   # True

# -----------------------------------
# MUTABLE: we can change an item
# -----------------------------------
my_list[0] = 99   # change the first element from 1 to 99
print("After changing index 0:", my_list)

# -----------------------------------
# DYNAMIC: we can add and remove items
# -----------------------------------

# Add an item to the end of the list
my_list.append("new item")
print("After append:", my_list)

# Remove the last item
last_item = my_list.pop()
print("Removed item:", last_item)
print("After pop:", my_list)

# =========================
# TUPLE vs LIST (important)
# =========================
# LIST uses square brackets: [ ]
# TUPLE uses parentheses:   ( )
#
# LIST  -> mutable (can change)
# TUPLE -> immutable (cannot change items)

# Your original "mu_list" line used parentheses, so it is a TUPLE, not a list:
mu_tuple = (1, 2, 3, 4, "hello", True)
print("mu_tuple (this is a TUPLE) =", mu_tuple)

# If you want "mu_list" to be a LIST, use square brackets:
mu_list = [1, 2, 3, 4, "hello", True]
print("mu_list (this is a LIST) =", mu_list)
