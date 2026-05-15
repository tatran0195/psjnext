---
title: "JPT.CastDItemToDCoord()"
description: "Convert DItem object to DCoord object to get the information of the selected coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ object to get the information of the selected coordinate system.

## Syntax

```psj
JPT.CastDItemToDCoord(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.

## Return Code

A _[DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ object (Coordinate system with relating information).

## Sample Code

```psj {16}
# Prepare model
Geometry.Part.Cube(iPartColor=6118844)
Tools.Coordinates.ThreeNode(crlNodes=[Node(454, 461, 462)])
Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(428, 436, 430)])
Tools.Coordinates.ThreeNode(strName="CCyl1", iCoordType=1, crlNodes=[Node(457, 474, 473)])
Tools.Coordinates.ThreeNode(strName="CSph1", iCoordType=2, crlNodes=[Node(316, 340, 333)])
Tools.Coordinates.ThreeNode(strName="CSph2", iCoordType=2, iOrder=3, crlNodes=[Node(190, 216, 204)])
JPT.ViewFitToModel()

# Get Coordinate object as DItem object from the created list of DItem objects
listDItemCoords = JPT.GetAllByTypeID(JPT.DItemType.COORD)
dItemCoord = listDItemCoords[0]
JPT.Debugger(dItemCoord)

# Convert from the above DItem object to DCoord object
dCoord = JPT.CastDItemToDCoord(dItemCoord)
JPT.Debugger(dCoord)
```
