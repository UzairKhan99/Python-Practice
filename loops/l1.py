# ============================
# LOOPS IN PYTHON (for, while)
# ============================
#
# A loop is used to repeat some code multiple times.

# =====================================
# 1) for loop with range (numbers)
# =====================================

print("=== for loop with range ===")

# range(start, stop) -> numbers from start up to (stop - 1)
# Here: 1, 2, 3, 4, 5
for i in range(1, 6):
    print("i =", i)

# You can also skip the start (default start = 0)
# range(5) -> 0, 1, 2, 3, 4
print("\nrange(5):")
for i in range(5):
    print("i =", i)


# =====================================
# 2) for loop over a list
# =====================================

print("\n=== for loop over a LIST ===")

numbers = [10, 20, 30, 40]

for n in numbers:
    print("Number:", n)

# Example: sum of all numbers in a list
print("\nSum of numbers in the list:")
total = 0
for n in numbers:
    total += n   # same as total = total + n

print("Total =", total)


# =====================================
# 3) for loop over a string
# =====================================

print("\n=== for loop over a STRING ===")

name = "Python"

for ch in name:
    print("Character:", ch)


# =====================================
# 4) while loop (runs while condition is True)
# =====================================

print("\n=== while loop (counting up) ===")

# while condition:
#     repeat this block

count = 1

while count <= 5:
    print("count =", count)
    count += 1   # same as count = count + 1

# When condition becomes False (count <= 5 is False),
# the loop stops.


print("\n=== while loop (counting down) ===")

num = 5

while num > 0:
    print("num =", num)
    num -= 1   # same as num = num - 1


# =====================================
# 5) break and continue
# =====================================

print("\n=== break in a loop ===")
# break -> immediately stop the loop

for i in range(1, 11):   # 1 to 10
    if i == 5:
        print("i is 5, breaking the loop")
        break
    print("i =", i)

# After break, we come out of the loop.


print("\n=== continue in a loop ===")
# continue -> skip the rest of this iteration and go to next

for i in range(1, 6):   # 1 to 5
    if i == 3:
        print("Skipping 3 using continue")
        continue
    print("i =", i)

# Notice: 3 is not printed with "i =", because that iteration is skipped.


# =====================================
# 6) Nested loops (loop inside a loop)
# =====================================

print("\n=== Nested loops ===")

for i in range(1, 4):          # outer loop: 1, 2, 3
    for j in range(1, 4):      # inner loop: 1, 2, 3
        print(f"i = {i}, j = {j}")
    print("--- end of inner loop for i =", i, "---")


# Quick summary (as comments):
# for variable in sequence:
#     # repeated code
#
# while condition:
#     # repeated code (runs while condition is True)
#
# break    -> stop the loop completely.
# continue -> skip current iteration, go to next.
