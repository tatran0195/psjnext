---
title: "Meshing.GridMesh()"
description: "Create a mesh with grid pattern for the selected faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > GridMesh"
---

## Description

Create a mesh with grid pattern for the selected faces.

## Syntax

```psj
Meshing.GridMesh(...)
```

## Inputs

<!-- @since:5.0.1 @type:List @required -->
### `listGridMesh`

- The parameters of Grid Mesh function (Refer to_[GRID\_MESH](./../../data-type/psj-command/parameter-types/GRID _MESH)_). Each parameter specifying an option of Grid Mesh funciton.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bProjectToCad`

- The used to enable/disable CAD projection. If this is enabled (_True_), after meshing, the meshed nodes is projected back to CAD model.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strGroupName`

- The name of a_[DGroup](../../data-type/psj-utility/pre-utility/built-in-types/DGroup)_ to contain the chosen target faces. If this parameter is left blank (""), no group will be created.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMakeNewGroup`

- Whether the function creates a new group or not:
  - _True_: Add all the meshed faces to a new group which will be created after executing the function.
  - _False_: Add all the meshed faces to the nearly created group after executing the function.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {4-32}
Geometry.Part.Cube(strName="Cube _2", iPartColor=5820248)
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

meshed _status = Meshing.GridMesh(listGridMesh=[GRID _MESH(crlFace=[Face(29)],
                                                         crlCorner=[Node(1838,
                                                                         1837,
                                                                         1387,
                                                                         1397)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID _MESH(crlFace=[Face(27)],
                                                         crlCorner=[Node(1837,
                                                                         1836,
                                                                         489,
                                                                         499)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID _MESH(crlFace=[Face(28)],
                                                         crlCorner=[Node(1386,
                                                                         1376,
                                                                         1836,
                                                                         1838)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID _MESH(crlFace=[Face(30)],
                                                         crlCorner=[Node(1837,
                                                                         1838,
                                                                         1836)],
                                                         ilMeshCount=[3],
                                                         iShape=3)],
                                 bProjectToCad=True,
                                 strGroupName="GridMeshFace")

JPT.Debugger(meshed _status)
```
