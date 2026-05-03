---
title: "Tools.Coordinates.ExportCoordinate()"
description: "Export local coordinates as Nastran bdf format."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Coordinates > Export Coordinate"
macro_link: ""
---

## Description

Export local coordinates as Nastran bdf format.

## Syntax

```psj
Tools.Coordinates.ExportCoordinate(...)
```

## Inputs

### `strlPath` @type(List\[String]) @default("")

- Path to import file.

## Return Code

A _Boolean_ specifying succeeded or not.

## Sample Code

```psj {18-20}
#Prepare model
Geometry.Part.Cube(iPartColor=6409934)

#Prepare coordinates
lcs1=Tools.Coordinates.ThreeNode(
    strName="CRect_1", 
    crlNodes=[Node(7, 6, 445)])

lcs2=Tools.Coordinates.ThreeNode(
    strName="CRect_2", 
    crlNodes=[Node(310, 317, 336)])

#Export coordinates

import os 
temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

Tools.Coordinates.ExportCoordinate(
    strlPath=os.path.join(temp_path,'exp-lcs.bdf'), 
    crlCS=[lcs1,lcs2])
```
