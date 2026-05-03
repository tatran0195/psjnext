---
title: "JPT.GetAllCoordinates()"
description: "Get all the information of all existing coordinate systems"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Get all the information of all existing coordinate systems.

## Syntax

```psj
JPT.GetAllCoordinates()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[CoordVector](../data-type/psj-utility/pre-utility/built-in-types/CoordVector)_ object or _List of [DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ objects containing all the information of all the existing coordinate systems.

## Sample Code

```psj {11}
# Prepare model
Geometry.Part.Cube(iPartColor=6118844)
Tools.Coordinates.ThreeNode(crlNodes=[Node(454, 461, 462)])
Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(428, 436, 430)])
Tools.Coordinates.ThreeNode(strName="CCyl1", iCoordType=1, crlNodes=[Node(457, 474, 473)])
Tools.Coordinates.ThreeNode(strName="CSph1", iCoordType=2, crlNodes=[Node(316, 340, 333)])
Tools.Coordinates.ThreeNode(strName="CSph2", iCoordType=2, iOrder=3, crlNodes=[Node(190, 216, 204)])
JPT.ViewFitToModel()

# Get all the existing coordinate systems
listDCoords = JPT.GetAllCoordinates()
JPT.Debugger(listDCoords)

# Print all the related information of each existing coordinate systems in list
for coord in listDCoords:
    JPT.Debugger(coord)
```
