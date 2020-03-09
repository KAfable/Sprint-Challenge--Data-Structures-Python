import time
from binary_search_tree import BinarySearchTree


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Loop Original

loop_duplicates = []
loop_start_time = time.time()

name_tree = BinarySearchTree('fake name')
for name in names_1:
    for name2 in names_2:
        if name == name2:
            loop_duplicates.append(name)

loop_end_time = time.time()
print(f"{len(loop_duplicates)} duplicates:\n\n{', '.join(loop_duplicates)}\n\n")
print(f"loop runtime: {loop_end_time - loop_start_time} seconds")


# BST Solution
bst_duplicates = []
bst_start_time = time.time()

name_tree = BinarySearchTree('fake name')
for name in names_1:
    name_tree.insert(name)

for name in names_2:
    if name_tree.contains_iteratively(name):
        bst_duplicates.append(name)

bst_end_time = time.time()
# print(f"{len(bst_duplicates)} duplicates:\n\n{', '.join(bst_duplicates)}\n\n")
print(
    f"BST runtime: {bst_end_time - bst_start_time} seconds, {len(bst_duplicates)} found")

# ---------- Stretch Goal -----------
# Dictionary Solution
dict_duplicates = []
dict_start_time = time.time()

dict1 = {name: 1 for name in names_1}
for name in names_2:
    if name in dict1:
        dict_duplicates.append(name)

dict_end_time = time.time()
# print(f"{len(dict_duplicates)} duplicates:\n\n{', '.join(dict_duplicates)}\n\n")
print(
    f"Dict runtime: {dict_end_time - dict_start_time} seconds, {len(dict_duplicates)} found")


# fast_duplicates = set(names_1+names_2)


# Set Solution
set_start_time = time.time()
names_1_set = set(names_1)
names_2_set = set(names_2)
set_duplicates = names_1_set.intersection(names_2_set)
set_end_time = time.time()
# print(f"{len(set_duplicates)} duplicates:\n\n{', '.join(set_duplicates)}\n\n")
print(
    f"Set runtime: {set_end_time - set_start_time} seconds {len(set_duplicates)} found")
