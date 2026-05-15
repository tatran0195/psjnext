---
title: "JPT.IsSpatialPointRendered()"
description: "Check if a specified point (node) that has the spatial coordinates (X, Y, Z) is rendered in the current view"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Check if a specified point (node) that has the spatial coordinates (X, Y, Z) is rendered in the current view.

## Syntax

```psj
JPT.IsSpatialPointRendered(posX, posY, posZ)
```

## Inputs

<!-- @since:5.1.0 @required -->
### posX

- Specify the X coordinate of the specified point (node).

<!-- @since:5.1.0 @required -->
### posY

- Specify the Y coordinate of the specified point (node).

<!-- @since:5.1.0 @required -->
### posZ

- Specify the Z coordinate of the specified point (node).

## Return Code

A _Boolean_ specifying the status of the specified point (node):

- _True_: The specified point (node) can be rendered.
- _False_: The specified point (node) is hidden.

## Sample Code

```psj {10}
# Prepare model
Geometry.Part.Cube(iPartColor=6974164)
JPT.ViewFitToModel()

# Select a node with ID = 7
JPT.SelectionByID(JPT.DItemType.NODE, 7, True)
listSelNodes = JPT.GetSelectedNodes()

# Check if the selected node is rendered
result=JPT.IsSpatialPointRendered(listSelNodes[0].pos.x, listSelNodes[0].pos.y, listSelNodes[0].pos.z)
print(result)
```
