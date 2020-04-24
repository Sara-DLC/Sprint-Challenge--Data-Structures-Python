import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# The original runtime of the 2 "for loops" would be O(n^2)
# original runtime == 6.719 seconds
'''
original code
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''
# Updated code with new runtime of under 2 seconds and O(n)
for name_1 in names_2:
    if names_1 == names_2:
        duplicates.append(names_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
