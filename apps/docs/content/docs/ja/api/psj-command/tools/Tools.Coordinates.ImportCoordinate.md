---
title: "Tools.Coordinates.ImportCoordinate()"
description: "Import local coordinates as Nastran BDF or ADVC ADX format.."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Coordinates > Import Coordinate"
macro _link: ""
---

## Description

Import local coordinates as Nastran BDF or ADVC ADX format.

## Syntax

```psj
Tools.Coordinates.ImportCoordinate(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strlPath

- Specify path to export file.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### crlCS

- Specify local coordinates.
- The default value is _None_.

## Return Code

A _Boolean_ specifying succeeded or not.

## Sample Code

```psj {28,29}
#Prepare model
Geometry.Part.Cube(iPartColor=6409934)

#Prepare coordinates
lcs1=Tools.Coordinates.ThreeNode(
    strName="CRect _1", 
    crlNodes=[Node(7, 6, 445)])

lcs2=Tools.Coordinates.ThreeNode(
    strName="CRect _2", 
    crlNodes=[Node(310, 317, 336)])

#Export coordinates

import os 
temp _path=JPT.GetAppPathInfo(JPT.PathType.TEMP _PATH)

Tools.Coordinates.ExportCoordinate(
    strlPath=os.path.join(temp _path,'exp-lcs.bdf'), 
    crlCS=[lcs1,lcs2])

#Delete the created coordinates

JPT.Exec(f"DeleteItem(0, [{lcs1},{lcs2}], [], [], 1)")

#Recreate coordinates by import coordinates exported before

Tools.Coordinates.ImportCoordinate(
    strlPath=os.path.join(temp _path,'exp-lcs.bdf'))
```
