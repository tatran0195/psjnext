---
title: "MainWindow.RightClick.SelectSurfaceColor()"
description: "Select faces that have the same color as the selected face."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > SelectSurfaceColor"
macro_link: "[SelectSurfaceColor](../../macro/main-window/SelectSurfaceColor)"
---

## Description

Select faces that have the same color as the selected face.

## Syntax

```psj
MainWindow.RightClick.SelectSurfaceColor(...)
```

## Inputs

### `crFace` @type(Cursor) @required

- That specify the target face.

### `bSelectFacesInSamePart` @type(Boolean)

- Value that defines the search scope.
  - _True_: Searches for faces with the same color within the part that contains the face specified in`crInput`.
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
    strName="Cube_2", 
    iPartColor=7434735
    )

# Change the color of the specified face (Face 21)
Assembly.RightClick.ChangeEntityColor(
    crlEntities=[Face(48, 50, 47, 21, 23, 22)], 
    iColor=16776960
    )

#Get faces with the same color as Face 21 in the entire model.
blue_faces = MainWindow.RightClick.SelectSurfaceColor(
    crFace=Face(21), 
    bSelectFacesInSamePart=False
    )
JPT.Debugger(blue_faces)

#Get faces with the same color as Face 21 within its part.
blue_faces_in_cube_1 = MainWindow.RightClick.SelectSurfaceColor(
    crFace=Face(21), 
    bSelectFacesInSamePart=True
    )
JPT.Debugger(blue_faces_in_cube_1)
```
