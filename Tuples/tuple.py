# =========================
# Python TUPLE – Basic Notes
# =========================
#
# Properties:
# 1) Immutable  -> cannot change items after creation
# 2) Heterogeneous -> can store different data types
# 3) Ordered   -> items keep their position
# 4) Made with parentheses () or tuple()
#
# Main difference from list:
# - LIST  -> [ ] and is MUTABLE (can change)
# - TUPLE -> ( ) and is IMMUTABLE (cannot change items)


# -----------------------------------
# 1) Creating tuples (different ways)
# -----------------------------------

# Using parentheses ()
t1 = (1, 2, 3)
print("t1:", t1)

# Heterogeneous tuple (different data types)
t2 = (1, 2.5, "hello", True)
print("t2:", t2)

# Tuple from a list using tuple()
my_list = [10, 20, 30]
t3 = tuple(my_list)
print("t3 (made from list):", t3)

# Single-element tuple (note the comma!)
t4 = (5,)   # this is a tuple
not_tuple = (5)  # this is just the number 5, not a tuple
print("t4 (single-element tuple):", t4)
print("not_tuple (just an int):", not_tuple)


print("\n============================")
print("ORDERED + INDEXING EXAMPLE")
print("============================")

# -----------------------------------
# 2) Ordered: access by index
# -----------------------------------
# Index:   0    1    2       3
t5 = ("a", "b", "c", "d")
print("t5:", t5)
print("Item at index 0:", t5[0])   # "a"
print("Item at index 2:", t5[2])   # "c"
print("Last item (index -1):", t5[-1])  # "d"


print("\n============================")
print("IMMUTABLE EXAMPLE")
print("============================")

# -----------------------------------
# 3) Immutable: cannot change items
# -----------------------------------
t6 = (1, 2, 3)
print("t6:", t6)

# The following line would cause an error if you uncomment it:
# t6[0] = 100
# TypeError: 'tuple' object does not support item assignment

print("You CANNOT do t6[0] = 100, because tuples are immutable.")


print("\n============================")
print("ALLOWED OPERATIONS")
print("============================")

# -----------------------------------
# 4) Some allowed operations on tuples
# -----------------------------------

t7 = (1, 2, 2, 3, 4)

# length of tuple
print("t7:", t7)
print("len(t7):", len(t7))

# count(value) -> how many times value appears
print("t7.count(2):", t7.count(2))  # 2 appears twice

# index(value) -> first position of value
print("t7.index(3):", t7.index(3))  # index of value 3

# slicing (like lists)
print("t7[1:4]:", t7[1:4])  # (2, 2, 3)


print("\n============================")
print("TUPLE VS LIST QUICK COMPARISON")
print("============================")

my_list = [1, 2, 3]       # list (mutable)
my_tuple = (1, 2, 3)      # tuple (immutable)

print("my_list:", my_list)
print("my_tuple:", my_tuple)

# You can change list:
my_list[0] = 100
print("After my_list[0] = 100 ->", my_list)

# You cannot change tuple:
print("You cannot do my_tuple[0] = 100 (it will give an error).")

# Summary (as comments):
# - Tuple is IMMUTABLE: no item assignment, no append, no remove.
# - Tuple is HETEROGENEOUS: can store different data types.
# - Tuple is ORDERED: you can use indexes.
# - Use () or tuple() to create tuples.
