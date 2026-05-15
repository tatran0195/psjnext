---
title: "Home.Windows.TileBox()"
description: "Display opening documents in vertical and horizontal arrangement like a box"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > Windows > TileBox"
macro _link: "[FrameLessBoxMode1](../../macro/home/FrameLessBoxMode1)"
---

## Description

Display opening documents in vertical and horizontal arrangement like a box.

## Syntax

```psj
Home.Windows.TileBox(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### iMode

- Specify the mode of arrangement.
  - 1: Mode 1.
  - 2: Mode 2.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {10}
# Prepare 2 JPT documents
Geometry.Part.Cube()
JPT.ViewFitToModel()
JPT.CreateNewDocument()
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube _2", iPartColor=6409934)
JPT.ViewFitToModel()

# Tile box arrangement
Home.Windows.TileBox(iMode=1)
```
