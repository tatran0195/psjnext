---
title: "Home.Windows.TileBox()"
description: "Display opening documents in vertical and horizontal arrangement like a box"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Home > Windows > TileBox"
macro_link: "[FrameLessBoxMode1](../../macro/home/FrameLessBoxMode1)"
---

## Description

Display opening documents in vertical and horizontal arrangement like a box.

## Syntax

```psj
Home.Windows.TileBox(...)
```

## Inputs

### `iMode` @type(Integer) @required

- The mode of arrangement.
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
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Tile box arrangement
Home.Windows.TileBox(iMode=1)
```
