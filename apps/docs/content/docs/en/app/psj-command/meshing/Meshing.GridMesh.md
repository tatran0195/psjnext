---
title: "Meshing.GridMesh()"
description: "Create a mesh with grid pattern for the selected faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > GridMesh"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a mesh with grid pattern for the selected faces.

## Syntax

```psj
Meshing.GridMesh(...)
```

## Inputs

### `listGridMesh` @type(List) @required

- The parameters of Grid Mesh function (Refer t&#x6F;_[GRID\_MESH](./../../data-type/psj-command/parameter-types/GRID_MESH)_). Each parameter specifying an option of Grid Mesh funciton.

### `bProjectToCad` @type(Boolean) @default(False)

- Used to enable/disable CAD projection. If this is enabled (_True_), after meshing, the meshed nodes is projected back to CAD model.

### `strGroupName` @type(String) @default("")

- The name of &#x61;_[DGroup](../../data-type/psj-utility/pre-utility/built-in-types/DGroup)_&#x74;o contain the chosen target faces. If this parameter is left blank (""), no group will be created.

### `bMakeNewGroup` @type(Boolean) @default(False)

- Whether the function creates a new group or not:
  - _True_: Add all the meshed faces to a new group which will be created after executing the function.
  - _False_: Add all the meshed faces to the nearly created group after executing the function.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {4-32}
Geometry.Part.Cube(strName="Cube_2", iPartColor=5820248)
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])

meshed_status = Meshing.GridMesh(listGridMesh=[GRID_MESH(crlFace=[Face(29)],
                                                         crlCorner=[Node(1838,
                                                                         1837,
                                                                         1387,
                                                                         1397)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID_MESH(crlFace=[Face(27)],
                                                         crlCorner=[Node(1837,
                                                                         1836,
                                                                         489,
                                                                         499)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID_MESH(crlFace=[Face(28)],
                                                         crlCorner=[Node(1386,
                                                                         1376,
                                                                         1836,
                                                                         1838)],
                                                         ilMeshCount=[3, 3],
                                                         iShape=4),
                                               GRID_MESH(crlFace=[Face(30)],
                                                         crlCorner=[Node(1837,
                                                                         1838,
                                                                         1836)],
                                                         ilMeshCount=[3],
                                                         iShape=3)],
                                 bProjectToCad=True,
                                 strGroupName="GridMeshFace")

JPT.Debugger(meshed_status)
```
