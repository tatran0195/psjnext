---
title: "MainWindow.RightClick.SelectByFace()"
description: "Select all targets in the same plane as the selected targets"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "MainWindow > RightClick > SelectByFace"
macro_link: "[ViewSelectByFace](../../macro/main-window/ViewSelectByFace)"
---

## Description

Select all targets in the same plane as the selected targets.

## Syntax

```psj
MainWindow.RightClick.SelectByFace(...)
```

## Inputs

### `iTargetType` @type(Integer) @required

- The target type to be selected.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The targets to select other targets in the same plane as them. The target can only be face or 2D element.

## Return Code

A _List of Cursor_ specifying the selected targets (faces or 2D elements)

## Sample Code

```psj {10}
# Prepare models
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
JPT.ViewFitToModel()
Assemble.AssembleFaceEx(ilPairFaceToMakeShareFace=[49, 24, 50, 75], dTolerance=0.0001, \
                        iTypeConnectPos=0, bFitEdge=True)

# Select all faces in the same plane as the specified face
listFaces = MainWindow.RightClick.SelectByFace(iTargetType=3, crlTargets=[Face(26)])
if listFaces is None:
    print("There is no selected faces")
elif len(listFaces) == 1:
    print("One face was selected")
    print(listFaces)
else:
    print(str(len(listFaces)) + " faces were selected")
    print(listFaces)
```
