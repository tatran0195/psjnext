---
title: "JPT.GetCurrentViewPoint()"
description: "Get all current settings of ViewPoint"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all current settings of ViewPoint.

## Syntax

```psj
JPT.GetCurrentViewPoint()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all settings of the currently displaying ViewPoint.

## Sample Code

```psj {2}
# Get all currently settings of ViewPoint
viewDict = JPT.GetCurrentViewPoint()

# Dump out result
pprint(viewDict)

# Print out the Scale factor
print("Scale Factor: " + str(viewDict["ScaleFactor"]))
```
