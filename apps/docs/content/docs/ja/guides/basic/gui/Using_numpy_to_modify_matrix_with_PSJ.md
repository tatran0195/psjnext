---
title: Use numpy to modify matrix with PSJ
description: This example demonstrates the way to use numpy for calculating some small examples
---

## 🎯 Introduction

In this tutorial, you'll learn how to use [_numpy library_](https://numpy.org/) for:

1. Making a matrix with size nx3 (n is number of nodes) containing nodal locations.
2. Returning the indices of the maximum values along an axis.
3. Sorting the matrix.
4. Calculating mean value in each row.

## 📖 Tutorial

```py
# Encoding for Japanese
# coding: cp932

import numpy as np

# Creating simple part
Geometry.Part.Cube()

# Creating an array
arr = np.array([[_.pos.x, _.pos.y, _.pos.z] for _ in JPT.GetAllNodes()])
print(arr.reshape(len(arr), 3))

# If no axis mentioned, then it works on the entire array
print(np.argmax(arr))

# If axis=1, then it works on each row
print(np.argmax(arr, axis=1))

# If axis=0, then it works on each column
print(np.argmax(arr, axis=0))

# Sort the whole array
print("Sort the whole array: \n" + str(np.sort(arr, axis=None)))

# Sort along each row
print("Sort along each row: \n" + str(np.sort(arr, axis=1)))

# Sort along each column
print("Sort along each column: \n" + str(np.sort(arr, axis=0)))

for i in range (len(arr)):
    print("--- Mean: " + str(np.mean(arr[i])))
```
