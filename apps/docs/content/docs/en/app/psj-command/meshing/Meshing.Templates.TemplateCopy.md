---
title: "Meshing.Templates.TemplateCopy()"
description: "Copy local mesh setting from one to another"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Meshing > Templates > TemplateCopy"
macro_link: "[TemplateCopy](../../macro/meshing/TemplateCopy)"
---

## Description

Copy local mesh setting from one to another.

## Syntax

```psj
Meshing.Templates.TemplateCopy(...)
```

## Inputs

### `crlReferent` @type(List\[Cursor]) @required

- The reference item (a Face or a Part). The local mesh setting set on this reference item will be copied.

### `crlTargets` @type(List\[Cursor]) @required

- The target item (a Face or a Part). The local mesh setting copied from reference item will be set on this target item if the two items are similar. Similarity conditions base on the selected`iMethod`.

### `iMethod` @type(Integer) @default(0)

- The method for similarity conditions.
  - If iMethod = 0: By Shape position: the two items are similar if their shape sizes are the same.
  - If iMethod = 1: By topology: the two items are similar if their topology classifications are the same.

### `iCopySub` @type(Integer) @default(1)

- To enable or disable the copy of local mesh setting on sub-items.
  - If selected target is Part, local mesh settings on Faces and Edges will be copied.
  - If selected target is Face, local mesh settings on Edges will be copied.

### `dTolerance` @type(Double) @default(0.001)

- The tolerance distance for similarity test.

### `strSource` @type(String) @default("")

- The name of the Jupiter doc to copy.

### `strTarget` @type(String) @default("")

- The name of the Jupiter doc to paste.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {16,17,18}
Geometry.Part.Cube(iPartColor=12999622)
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])
Meshing.LocalSettings.Face(strName="MeshParam_1",
                           localMesh=LOCAL_MESH(iEntityType=2,
                                                bEnableSizeParams=True,
                                                dAvgElemSize=0.002,
                                                dMaxElemSize=0.01,
                                                dMinElemSize=0.001,
                                                bEnableMeshPattern=True,
                                                iMeshPatternType=1),
                           crlTargets=[Face(27, 28, 29)])

Geometry.Part.Cube(strName="Cube_2", iPartColor=7731705)
Geometry.MakeFillet(crlEdges=[Edge(93, 90, 94)])

copy_status = Meshing.Templates.TemplateCopy(crlReferent=[Part(1)],
                                             crlTargets=[Part(2)],
                                             dTolerance=1e-06)

JPT.Debugger(copy_status)
```

:::info

Example of window to window case.

```psj {3,4,5}
Geometry.Part.Cube()
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])
Meshing.Templates.TemplateCopy(dTolerance=1e-06,
                               strSource="Jupiter2",
                               strTarget="Jupiter1")
```

In this example, \[Jupiter2] window will have the same local mesh setting with the \[Jupiter1] window.

:::
