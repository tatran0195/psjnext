---
title: "JPT.GetCurrentContour()"
description: "Get all current settings of Contour"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get all current settings of Contour.

## Syntax

```psj
JPT.GetCurrentContour()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all settings of the currently displaying Contour.

## Sample Code

```psj {2}
# Get all currently settings of Contour
contourDict = JPT.GetCurrentContour()

# Dump out result
pprint(contourDict)

# Print out the Upper color
colorRGB = JPT.ConvertJPTColorToRGB(contourDict["UpperColor"])
print("Upper Color: " + colorRGB)
```
