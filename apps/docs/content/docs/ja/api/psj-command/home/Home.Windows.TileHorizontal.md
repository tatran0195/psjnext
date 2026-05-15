---
title: "Home.Windows.TileHorizontal()"
description: "Display opening documents in a horizontal arrangement"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > Windows > TileHorizontal"
macro _link: "[TileHorizontal](../../macro/home/TileHorizontal)"
---

## Description

Display opening documents in a horizontal arrangement.

## Syntax

```psj
Home.Windows.TileHorizontal(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### iMode

- Specify the horizontal mode of arrangement.
  - 0: Tile Horizontal.
  - 1: Mode 1.
  - 2: Mode 2.
  - 3: Mode 3.
  - 4: Mode 4.
  - 5: Mode 5.
  - 6: Mode 6.
  - 7: Mode 7.

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

# Tile horizontal arrangement
Home.Windows.TileHorizontal(iMode=0)
```
