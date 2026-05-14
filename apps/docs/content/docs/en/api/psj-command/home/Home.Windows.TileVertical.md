---
title: "Home.Windows.TileVertical()"
description: "Display opening documents in a vertical side-by-side arrangement"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Home > Windows > TileVertical"
macro _link: "[TileVertical](../../macro/home/TileVertical)"
---

## Description

Display opening documents in a vertical side-by-side arrangement.

## Syntax

```psj
Home.Windows.TileVertical(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @required -->
### `iMode`

- The vertical mode of arrangement.
  - 0: Tile Vertical.
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

# Tile vertical arrangement
Home.Windows.TileVertical(iMode=0)
```
