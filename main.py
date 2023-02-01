from listset import ListSet
from sorted_listset import SortedListSet
from fileset import FileSet

import random
import timeit

MENU = "Enter the implementation you want to test (1=ListSet, 2=SortedListSet, 3=FileSet): "

NUM_SET_ITEMS = 10000
ITEM_VALUE_DOMAIN = NUM_SET_ITEMS * 10
NUM_TESTS = 1000

choice = int(input(MENU))
while choice not in [1, 2, 3]:
    print("Choice not recognized")
    choice = int(intput(MENU))

if choice == 1:
    s = ListSet()
elif choice == 2:
    s = SortedListSet()
else:
    s = FileSet("set.txt")

print("Generating the set...")
for i in range(NUM_SET_ITEMS):
    # Task 4, Step 1
    pass

print("Generating the test cases...")
test_samples = []
for i in range(NUM_TESTS):
    # Task 4, Step 2
    pass

print("Benchmarking contains()...")
total_time = 0
for sample in test_samples:
    # Task 4, Step 3
    total_time += timeit.timeit('pass', number=1, globals=globals())

# Task 4, Step 4