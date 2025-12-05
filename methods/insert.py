# =====================================
# List Methods: insert, remove, pop
# =====================================

# ------------------------
# 1) insert(index, value)
# ------------------------
# insert adds a new item at a specific position.
# Syntax: list.insert(index, value)
# - index: where to put the new item
# - value: what to insert

a = [1, 2, 3]
print("INSERT EXAMPLE")
print("Original a:", a)

a.insert(0, "Hi coders")   # put "Hi coders" at index 0 (the beginning)
print("After a.insert(0, 'Hi coders'):", a)
print("-" * 40)


# ------------------------
# 2) remove(value)
# ------------------------
# remove deletes the FIRST matching value from the list.
# Syntax: list.remove(value)
# - If the value is not in the list, Python gives an error.

a = [1, 2, 3]
print("REMOVE EXAMPLE")
print("Original a:", a)

a.remove(3)     # remove the value 3 (not index 3)
print("After a.remove(3):", a)

# Example: removing a string value
b = ["apple", "banana", "apple"]
print("Original b:", b)
b.remove("apple")   # removes the FIRST "apple"
print("After b.remove('apple'):", b)
print("-" * 40)


# ------------------------
# 3) pop([index])
# ------------------------
# pop removes and returns an item from the list.
# Syntax:
#   list.pop()        -> removes and returns the LAST item
#   list.pop(index)   -> removes and returns the item at that index
# If index is out of range, Python gives an error.

# Example: pop() without index (removes last item)
a = [10, 20, 30, 40]
print("POP EXAMPLE (without index)")
print("Original a:", a)

last_item = a.pop()   # removes 40
print("Returned by a.pop():", last_item)
print("List after a.pop():", a)
print()

# Example: pop(index) with index (removes specific position)
a = [10, 20, 30, 40]
print("POP EXAMPLE (with index)")
print("Original a:", a)

first_item = a.pop(0)     # removes item at index 0 (10)
print("Returned by a.pop(0):", first_item)
print("List after a.pop(0):", a)

middle_item = a.pop(1)    # removes item at index 1 (now 30)
print("Returned by a.pop(1):", middle_item)
print("List after a.pop(1):", a)
print("-" * 40)


# Quick summary (as comments):
# insert(index, value) -> add item at a position, does not remove anything.
# remove(value)       -> delete the FIRST occurrence of that value.
# pop([index])        -> delete item (last by d
