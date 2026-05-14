---
title: "JPT.ConvertCoordinateFromGlobalToLocal()"
description: "Convert coordinate from global to local"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Convert global coordinate of selected DItem Type into specified local coordinate.

## Syntax

```psj
JPT.ConvertCoordinateFromGlobalToLocal(DItemType, itemID, DCoord)
```

## Inputs

<!-- @since:5.1.0 @type:DItemType @required -->
### `DItemType`

- The _[DItemType](../data-type/psj-command/DItem-types)_ of BODY, FACE, ELEMENT, EDGE, or NODE entity in Jupiter.

<!-- @since:5.1.0 @type:Integer @required -->
### `itemID`

- The ID of the target entity.

<!-- @since:5.1.0 @type:DCoord @required -->
### `DCoord`

- The object specifying Coordinate System which will be used to convert.

## Return Code

A _[DItemPair](../data-type/psj-utility/pre-utility/built-in-types/DItemPair)_ object specifying the information of target entity according to the converted Coordinate System.

- `firstDItem` is an _integer_ specifying the Node IDs of target entity.
- `secondDItem` is a _[TVector3d](../data-type/psj-utility/pre-utility/built-in-types/TVector3d)_ object specifying the coordinates of the corresponding node according to the converted Coordinate System.

## Sample Code

```psj {9}
# Prepare model and local coordinate
Geometry.Part.Cube()
JPT.ViewFitToModel()
Tools.Coordinates.ThreeNode(crlNodes=[Node(488, 96, 88)])

# Get all local coordinates
# And convert global coordinate of specified DItemType.NODE into the selected local coordinate
listCoords = JPT.GetAllCoordinates()
convertCoord = JPT.ConvertCoordinateFromGlobalToLocal(JPT.DItemType.NODE, 8, listCoords[0])


# Get node ID and coordinates of DItem.NODE object according to the converted Coordinate System
JPT.Debugger(convertCoord[0].first)
JPT.Debugger(convertCoord[0].second)
```
