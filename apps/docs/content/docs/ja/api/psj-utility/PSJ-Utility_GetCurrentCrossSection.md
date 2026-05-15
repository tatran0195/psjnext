---
title: "JPT.GetCurrentCrossSection()"
description: "Get all current settings of Cross Section"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all current settings of Cross Section.

## Syntax

```psj
JPT.GetCurrentCrossSection()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all settings of the currently displaying Cross Section.

## Sample Code

```psj {2}
# Get all currently settings of Cross Section
crossDict = JPT.GetCurrentCrossSection()

# Dump out result
pprint(crossDict)

# Print out the current position
print("Current Position: " + str(crossDict["CurrentPosition"]))
```
