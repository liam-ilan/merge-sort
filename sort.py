# libraries
import random
import math

# merge
# gets two arrays, orrdered arrays
# returns a single, ordered array
def merge(arr1, arr2):

  # our result
  result = []

  # itterate for a maximum of len(arr1) + len(arr2) times
  for x in range(0, len(arr1) + len(arr2)):

    # if one of the arrays is empty, break the loop
    if len(arr1) == 0 or len(arr2) == 0:
      break

    # compare the first item from arr1 and arr2
    # if arr1[0] is smaller, add it to the result, else, add arr2[0] to the result
    if arr1[0] > arr2[0]:
      result.append(arr2[0])
      arr2.pop(0)
    else:
      result.append(arr1[0])
      arr1.pop(0)

  # add the remaining items
  for x in range(0, len(arr1)):
    result.append(arr1[x])

  for x in range(0, len(arr2)):
    result.append(arr2[x])

  # return result
  return result

# mergeSort
# gets an array of arrays of ordered items
# returns a sorted array nested in a sorted array
def mergeSort(arr):

  # out result
  result = []

  # merge every two items
  for x in range(0, math.floor(len(arr) / 2)):
    result.append(merge(arr[x * 2], arr[x * 2 + 1]))

  # odd length case
  if len(arr) % 2 == 1:
    result.append(arr[-1])

  # recursivly loop over result
  if not (len(result) == 1):
    result = mergeSort(result)

  # return result
  return result
  
# sort
# gets an array
# nests and unpacks the array for mergeSort
def sort(arr):
  return mergeSort([[arr[x]] for x in range(0, len(arr))])[0]

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
