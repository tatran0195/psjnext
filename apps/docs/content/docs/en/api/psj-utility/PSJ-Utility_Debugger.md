---
title: "JPT.Debugger()"
description: "Console debugger for PSJ"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Console debugger for PSJ. This utility will show all the related information of the inputted value to the Python API window.

## Syntax

```psj
JPT.Debugger(inputValue)
```

## Inputs

### `inputValue`

- A value needing to know its information.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {6}
# Prepare model
Geometry.Part.Cube()
# Get the information of all existing parts
allParts = JPT.GetAllParts()
# Print all the related information of the first part to the screen
JPT.Debugger(allParts[0])
```
