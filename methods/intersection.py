# ==================================
# SETS and NESTED LISTS in Python
# ==================================

# =====================
# 1) SETS – Basic Idea
# =====================
# A set:
#   - Unordered collection (no fixed index positions)
#   - Contains UNIQUE items (duplicates are removed)
#   - Created using { } or set(iterable)

a = [1, 2, 3]
b = [4, 2, 3]

# Correct ways to make sets:

# From a list:
s1 = set(a)       # set from list a -> {1, 2, 3}
s2 = set(b)       # set from list b -> {2, 3, 4}

print("SET EXAMPLES")
print("List a:", a)
print("List b:", b)
print("Set s1 (from a):", s1)
print("Set s2 (from b):", s2)

# NOTE: set(4) is WRONG because 4 is not an iterable.
# You can do {4} to make a set with one element:
single_set = {4}
print("Single-element set {4}:", single_set)


# ------------------------
# Set Intersection
# ------------------------
# intersection() gives common elements between sets.

s3 = s1.intersection(s2)
print("\nINTERSECTION EXAMPLE")
print("s1:", s1)
print("s2:", s2)
print("s1 ∩ s2 (common elements):", s3)   # should be {2, 3}

# Other common set operations (for reference):
# union:        s1.union(s2)        -> all elements from both sets
# difference:   s1.difference(s2)   -> in s1 but not in s2
# symmetric_difference: s1.symmetric_difference(s2) -> in one but not both


print("\n=====================")
print("2) NESTED LISTS")
print("=====================")

# ==========================
# 2) NESTED LISTS – Basics
# ==========================
# A "nested list" is a list that CONTAINS another list inside it.

# Simple list
a = [1, 2, 3]
print("List a:", a)

# Nested list (list inside a list)
b = [1, 2, 3, [7, 8, 8]]
print("Nested list b:", b)

# Index positions in b:
# b[0] -> 1
# b[1] -> 2
# b[2] -> 3
# b[3] -> [7, 8, 8]   (this is an inner list)

print("\nACCESSING NESTED ELEMENTS")

# Access the inner list:
inner_list = b[3]
print("b[3] (inner list):", inner_list)      # [7, 8, 8]

# Access elements inside the inner list:
# inner_list[0] -> 7
# inner_list[1] -> 8
# inner_list[2] -> 8

print("b[3][0]:", b[3][0])   # 7
print("b[3][1]:", b[3][1])   # 8
print("b[3][2]:", b[3][2])   # 8

# Another way to see it:
x = b[3][0]   # first element of the inner list
y = b[3][1]   # second element
z = b[3][2]   # third element

print("\nValues from inner list:")
print("x (b[3][0]):", x)
print("y (b[3][1]):", y)
print("z (b[3][2]):", z)


print("\nMORE NESTED LIST EXAMPLE")

# List of lists (each element is a list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("matrix:", matrix)
print("matrix[0]:", matrix[0])      # [1, 2, 3]
print("matrix[1]:", matrix[1])      # [4, 5, 6]
print("matrix[2]:", matrix[2])      # [7, 8, 9]

# Access single elements:
print("matrix[0][0]:", matrix[0][0])  # 1
print("matrix[1][2]:", matrix[1][2])  # 6
print("matrix[2][1]:", matrix[2][1])  # 8

# Quick summary (as comments):
# SET:
#   - Use { } or set(iterable)
#   - No duplicates, no order, supports operations like intersection, union.
#
# NESTED LIST:
#   - A list inside a list.
#   - Use multiple indexes like list[i][j] to reach inner elements.
