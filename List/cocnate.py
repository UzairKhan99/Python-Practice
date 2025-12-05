# ==================================
# Joining (concatenating) two lists
# ==================================
#
# Using + with lists:
#   new_list = list_a + list_b
#
# This:
#   - Creates a NEW list
#   - Puts all elements of list_a first
#   - Then all elements of list_b
#   - Does NOT change the original lists

lst_1 = [1, 2, 3, 4, 5]
lst_2 = [6, 4, 7, 5, 9]

print("lst_1:", lst_1)
print("lst_2:", lst_2)

# Concatenate (join) the two lists
list_ans = lst_1 + lst_2

print("\nAfter concatenation (lst_1 + lst_2):")
print("list_ans:", list_ans)   # [1, 2, 3, 4, 5, 6, 4, 7, 5, 9]

# Check that original lists are unchanged
print("\nlst_1 (unchanged):", lst_1)
print("lst_2 (unchanged):", lst_2)

# -------------------------------------------
# Extra: other ways to combine lists (for info)
# -------------------------------------------

# 1) Using extend() to add lst_2 into lst_1
lst_3 = [1, 2, 3, 4, 5]
lst_4 = [6, 4, 7, 5, 9]

lst_3.extend(lst_4)   # changes lst_3
print("\nUsing extend():")
# [1, 2, 3, 4, 5, 6, 4, 7, 5, 9]
print("lst_3 after lst_3.extend(lst_4):", lst_3)
print("lst_4 (unchanged):", lst_4)

# 2) Using * to repeat a list
lst_5 = [1, 2, 3]
repeated = lst_5 * 3
print("\nUsing * to repeat a list:")
print("lst_5:", lst_5)
print("repeated (lst_5 * 3):", repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Quick summary (as comments):
# lst_1 + lst_2  -> returns a NEW list with elements of both.
# list1.extend(list2) -> modifies list1 by adding elements of list2.
# list * n -> repeats the list n times.
