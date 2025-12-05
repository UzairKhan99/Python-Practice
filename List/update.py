# =====================================
# Updating list items & Slicing in Python
# =====================================

# Note: Do not use the name "list" as a variable,
# because list is a built-in type in Python.
# Use names like lst or my_list instead.

print("=== SIMPLE UPDATE (INDEX ASSIGNMENT) ===")

lst = [1, 2, 3, 4]
print("Original lst:", lst)

# -------------------------
# Update (change) one element by index
# -------------------------
# lst[index] = new_value
# index 0 -> first element

lst[0] = "hello"   # change first element from 1 to "hello"
print("After lst[0] = 'hello':", lst)

# You can update any index (as long as it exists)
lst[2] = 999       # change the element at index 2
print("After lst[2] = 999:", lst)

print("\n=== SLICING (READING SLICES) ===")

# Slicing syntax:
# lst[start:stop]
# - start index is included
# - stop index is excluded (not included)
# - if start is omitted, it defaults to 0
# - if stop is omitted, it goes to the end of the list

my_list = [1, 2, 3, 4, 5]
print("my_list:", my_list)

print("my_list[0:3]:", my_list[0:3])  # elements at indexes 0,1,2 -> [1, 2, 3]
print("my_list[1:4]:", my_list[1:4])  # indexes 1,2,3 -> [2, 3, 4]
print("my_list[:3]:", my_list[:3])    # same as [0:3] -> [1, 2, 3]
print("my_list[2:]:", my_list[2:])    # from index 2 to end -> [3, 4, 5]

print("\n=== SLICE ASSIGNMENT (UPDATING MULTIPLE ITEMS) ===")

# Your example:
lst2 = [1, 2, 3]
print("Original lst2:", lst2)

# -------------------------
# Slice assignment:
# lst2[start:stop] = [new, values, here]
#
# This replaces the items in the slice with the new list.
# The number of new items does NOT have to equal the number of old items.
# Python will resize the list automatically.
# -------------------------

lst2[0:3] = [10, 12, "Uzair"]
print("After lst2[0:3] = [10, 12, 'Uzair']:", lst2)
# All elements were replaced because [0:3] covered the whole list.

# More slice assignment examples:

print("\nMore slice assignment examples:")

lst3 = [1, 2, 3, 4, 5]
print("Original lst3:", lst3)

# Replace middle two elements (indexes 1 and 2)
lst3[1:3] = [20, 30]
print("After lst3[1:3] = [20, 30]:", lst3)   # [1, 20, 30, 4, 5]

# Replace a slice with more items (list grows)
lst3[2:4] = [300, 400, 500]
print("After lst3[2:4] = [300, 400, 500]:", lst3)

# Replace a slice with fewer items (list shrinks)
lst3[1:5] = [999]
print("After lst3[1:5] = [999]:", lst3)

# Quick summary (as comments):
# - lst[i] = value           -> update a single element.
# - lst[start:stop]          -> read a slice (subset) of the list.
# - lst[start:stop] = [...]  -> replace that slice with new values (can change list size).
