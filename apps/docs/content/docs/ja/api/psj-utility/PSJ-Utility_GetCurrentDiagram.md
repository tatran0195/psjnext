---
title: "JPT.GetCurrentDiagram()"
description: "Get all current settings of Diagram"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all current settings of Diagram.

## Syntax

```psj
JPT.GetCurrentDiagram()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all settings of the currently displaying Diagram.

## Sample Code

```psj {2}
# Get all currently settings of Diagram
diagramDict = JPT.GetCurrentDiagram()

# Dump out result
pprint(diagramDict)

# Print out the Positive color
colorRGB = JPT.ConvertJPTColorToRGB(diagramDict["PositiveColor"])
print("Positive Color: " + colorRGB)
```
