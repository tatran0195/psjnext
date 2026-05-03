---
title: "Tools.Coordinates.ImportCoordinate()"
description: "Import local coordinates as Nastran BDF or ADVC ADX format.."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Tools > Coordinates > Import Coordinate"
macro_link: ""
---

## Description

Import local coordinates as Nastran BDF or ADVC ADX format.

## Syntax

```psj
Tools.Coordinates.ImportCoordinate(...)
```

## Inputs

### `strlPath` @type(List\[String]) @default("")

- Path to export file.

### `crlCS` @type(List\[Cursor]) @default(None)

- Local coordinates.

## Return Code

A _Boolean_ specifying succeeded or not.

## Sample Code

```psj {28,29}
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

#Delete the created coordinates

JPT.Exec(f"DeleteItem(0, [{lcs1},{lcs2}], [], [], 1)")

#Recreate coordinates by import coordinates exported before

Tools.Coordinates.ImportCoordinate(
    strlPath=os.path.join(temp_path,'exp-lcs.bdf'))
```
