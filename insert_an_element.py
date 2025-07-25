import numpy as np
l = np.array(list(map(int, input("Enter list elements: ").split()))
data, index = [int(x) for x in input("Enter data and index: ").split()]
index -= 1
modified = np.insert(l, index, data)
print("Original array:", l)
print("Modified array:", modified)
