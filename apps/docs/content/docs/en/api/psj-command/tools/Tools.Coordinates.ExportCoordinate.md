---
title: "Tools.Coordinates.ExportCoordinate()"
description: "Export local coordinates as Nastran bdf format."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Tools > Coordinates > Export Coordinate"
macro _link: ""
---

## Description

Export local coordinates as Nastran bdf format.

## Syntax

```psj
Tools.Coordinates.ExportCoordinate(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[String] @optional @default:"" -->
### `strlPath`

- The path to import file.

## Return Code

A _Boolean_ specifying succeeded or not.

## Sample Code

```psj {18-20}
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
```
