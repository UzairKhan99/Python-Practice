# ==========================================
# List methods: clear, index, count, sort,
# and built-ins: min, max
# ==========================================

# Note:
# You do NOT need to import anything to use
# list methods like index(), count(), sort(), clear().
# Just use them directly on the list.

# ------------------------
# 1) clear()
# ------------------------
# clear() removes ALL elements from the list.
# After clear(), the list becomes empty: []

a = [1, 2, 33, 4]
print("CLEAR EXAMPLE")
print("Original a:", a)

a.clear()   # remove all items
print("After a.clear():", a)   # [] (empty list)
print("-" * 40)


# ------------------------
# 2) index(value)
# ------------------------
# index(value) returns the POSITION (index)
# of the FIRST occurrence of the value in the list.
# If the value is not found, Python raises an error.

a = [1, 2, 33, 4]
print("INDEX EXAMPLE")
print("List a:", a)

pos_33 = a.index(33)   # find index of value 33
print("Index of 33 in a:", pos_33)  # should print 2
print("-" * 40)


# ------------------------
# 3) count(value)
# ------------------------
# count(value) returns how many times the value
# appears in the list.

count_list = [1, 2, 3, 4, 1, 1, 1, 1, 1, 1]
print("COUNT EXAMPLE")
print("count_list:", count_list)

counter = count_list.count(1)   # count how many 1's
print("Number of times 1 appears:", counter)
print("-" * 40)


# ------------------------
# 4) sort()
# ------------------------
# sort() arranges the list items in increasing (ascending) order.
# It changes the original list (in-place).
#
# For example, numbers will be sorted from smallest to largest.
# Do not mix unrelated types (e.g., numbers and strings) in the same list
# if you want to sort, or you'll get an error in Python 3.

a = [90, 50, -1.5, 5, 4, 6]
print("SORT EXAMPLE")
print("Original a:", a)

a.sort()   # sort in ascending order
print("After a.sort():", a)

# You can also sort in descending order using reverse=True:
a.sort(reverse=True)
print("After a.sort(reverse=True):", a)
print("-" * 40)


# ------------------------
# 5) min() and max()
# ------------------------
# min(list) -> smallest value in the list
# max(list) -> largest value in the list
#
# These are built-in functions, not list methods.
# You pass the list as an argument.

b = [10, 200, -5, 7, 50]
print("MIN / MAX EXAMPLE")
print("List b:", b)

print("Minimum value in b:", min(b))   # -5
print("Maximum value in b:", max(b))   # 200
print("-" * 40)

# Quick summary (as comments):
# clear()         -> remove all items, list becomes empty.
# index(value)    -> get index (position) of FIRST occurrence of value.
# count(value)    -> how many times value appears in list.
# sort()          -> sort list in-place (ascending by default).
# min(list)       -> smallest element of the list.
# max(list)       -> largest element of the list.
