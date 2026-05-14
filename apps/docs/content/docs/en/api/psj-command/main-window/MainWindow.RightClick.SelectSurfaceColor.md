---
title: "MainWindow.RightClick.SelectSurfaceColor()"
description: "Select faces that have the same color as the selected face."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "MainWindow > RightClick > SelectSurfaceColor"
macro _link: "[SelectSurfaceColor](../../macro/main-window/SelectSurfaceColor)"
---

## Description

Select faces that have the same color as the selected face.

## Syntax

```psj
MainWindow.RightClick.SelectSurfaceColor(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @required -->
### `crFace`

- The specify the target face.

<!-- @since:5.1.0 @type:Boolean @optional -->
### `bSelectFacesInSamePart`

- The value that defines the search scope.
  - _True_: Searches for faces with the same color within the part that contains the face specified in `crInput`.
  - _False_: Searches for faces with the same color across the entire model.

## Return Code

- A list of _Cursor_ (string format) for the detected faces.

## Sample Code

```psj {18-22, 25-28}
#Prepare Model
Geometry.Part.Cube(
    iPartColor=6409934
    )

Geometry.Part.Cube( 
    dlOrigin=[0.02, 0.0, 0.0], 
    strName="Cube _2", 
    iPartColor=7434735
    )

# Change the color of the specified face (Face 21)
Assembly.RightClick.ChangeEntityColor(
    crlEntities=[Face(48, 50, 47, 21, 23, 22)], 
    iColor=16776960
    )

#Get faces with the same color as Face 21 in the entire model.
blue _faces = MainWindow.RightClick.SelectSurfaceColor(
    crFace=Face(21), 
    bSelectFacesInSamePart=False
    )
JPT.Debugger(blue _faces)

#Get faces with the same color as Face 21 within its part.
blue _faces _in _cube _1 = MainWindow.RightClick.SelectSurfaceColor(
    crFace=Face(21), 
    bSelectFacesInSamePart=True
    )
JPT.Debugger(blue _faces _in _cube _1)
```
