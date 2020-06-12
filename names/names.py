import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value == self.value:
            # if value not in duplicates:
            #     duplicates.append(value)
            self.right = Node(value)
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        if value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        if target == self.value:
            duplicates.append(self.value)
        if self.value == None:
            return False
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if self.left is None:
            return False
        else:
            return self.left.contains(target)

# no_dupes = Node("Name")

# for n1 in names_1:
#     no_dupes.insert(n1)
# for n2 in names_2:
#     no_dupes.insert(n2)

# dupes = Node("Jean Velazquez")

# for n1 in names_1:
#     dupes.insert(n1)

# for x in names_2:
#     dupes.contains(x)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
