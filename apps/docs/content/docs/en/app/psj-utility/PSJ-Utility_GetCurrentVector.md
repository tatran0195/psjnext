---
title: "JPT.GetCurrentVector()"
description: "Get all current settings of Vector"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get all current settings of Vector.

## Syntax

```psj
JPT.GetCurrentVector()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all settings of the currently displaying Vector.

## Sample Code

```psj {2}
# Get all currently settings of Vector
vectorDict = JPT.GetCurrentVector()

# Dump out result
pprint(vectorDict)

# Print out the Positive color
colorRGB = JPT.ConvertJPTColorToRGB(vectorDict["PositiveColor"])
print("Positive Color: " + colorRGB)
```
