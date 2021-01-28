import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height = np.array(height)
# print(type(np_height))

weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_weight = np.array(weight)
# print(type(np_weight))

bmi = np_weight/np_height ** 2
print(type(bmi))
print(bmi)




# numpy arrays assume values of only one type - otherwise will do a "type
#   coercion" and change all values to a single type

# numpy arrays are their own data type, operators will act differently

plist = [1,2,3]
print(plist + plist)
# [1, 2, 3, 1, 2, 3]

numpy_array = np.array([1,2,3])
print(numpy_array + numpy_array)
# [2 4 6]

# arrays have indexes, but can also be "Boolean'ed"
print(bmi[1]) 
# 20.97505668934241

print(bmi > 23)
# [False False False  True False]

print(bmi[bmi > 23])
# array([24.7473475])
# ^^ returns the items in the array for which the statement is True
