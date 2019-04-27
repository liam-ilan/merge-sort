# import sort from sort.py
from sort import *

# import random
import random

# randomArray
# gets a length and a limit
# generates a random array with a specified length, filled with random ints less than, or equal to the limit
def randomArray(length, limit):
  return [random.randint(0, limit) for x in range(0, length)]

# sort a random array, with a given length
array = randomArray(int(input()), 100)
print (array)
print (' | \n | \n\\ /')
print(sort(array))
