# ============================
# range() – Basic Explanation
# ============================
#
# range is used to generate a sequence of integers.
# It works ONLY with integers.
#
# Forms:
#   range(stop)
#   range(start, stop)
#   range(start, stop, step)
#
# IMPORTANT:
# - start: first number (INCLUSIVE)
# - stop:  last limit (EXCLUSIVE → not included)
# - step:  difference between numbers
#
# Examples:
#   range(5)            -> 0, 1, 2, 3, 4
#   range(1, 5)         -> 1, 2, 3, 4
#   range(1, 10, 2)     -> 1, 3, 5, 7, 9


print("=== BASIC range(stop) EXAMPLE ===")
r1 = range(5)     # 0, 1, 2, 3, 4
print("r1:", r1)  # range object
print("list(r1):", list(r1))  # convert to list to see the numbers


print("\n=== range(start, stop) EXAMPLE ===")
r2 = range(1, 6)  # 1, 2, 3, 4, 5
print("r2:", r2)
print("list(r2):", list(r2))


print("\n=== range(start, stop, step) EXAMPLE ===")
# Your example:
number = range(1, 1000, 1)           # from 1 up to 999
list_num = list(range(1, 1000, 1))   # convert to list

print("First 10 numbers of list_num:", list_num[:10])   # show only first 10
print("Last 5 numbers of list_num:", list_num[-5:])     # show last 5


print("\n=== STEP > 1 EXAMPLE ===")
r3 = range(0, 10, 2)   # 0, 2, 4, 6, 8
print("range(0, 10, 2):", list(r3))


print("\n=== NEGATIVE STEP EXAMPLE ===")
# Counting backwards:
r4 = range(10, 0, -1)  # 10, 9, 8, ..., 1
print("range(10, 0, -1):", list(r4))


print("\n=== USING range IN A for LOOP ===")
# range is usually used in for loops:

print("Numbers from 1 to 5 using for-loop:")
for i in range(1, 6):
    print(i)

# Quick summary (as comments):
# - range generates integers in a sequence.
# - stop is NOT included.
# - step can be positive or negative (but not 0).
# - Use list(range(...)) if you want to see all values at once.
