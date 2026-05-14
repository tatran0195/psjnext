---
title: "Meshing.Templates.TemplateCopy()"
description: "Copy local mesh setting from one to another"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Meshing > Templates > TemplateCopy"
macro _link: "[TemplateCopy](../../macro/meshing/TemplateCopy)"
---

## Description

Copy local mesh setting from one to another.

## Syntax

```psj
Meshing.Templates.TemplateCopy(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlReferent`

- The reference item (a Face or a Part). The local mesh setting set on this reference item will be copied.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target item (a Face or a Part). The local mesh setting copied from reference item will be set on this target item if the two items are similar. Similarity conditions base on the selected`iMethod`.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method for similarity conditions.
  - If iMethod = 0: By Shape position: the two items are similar if their shape sizes are the same.
  - If iMethod = 1: By topology: the two items are similar if their topology classifications are the same.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCopySub`

- The to enable or disable the copy of local mesh setting on sub-items.
  - If selected target is Part, local mesh settings on Faces and Edges will be copied.
  - If selected target is Face, local mesh settings on Edges will be copied.

<!-- @since:5.0.1 @type:Double @optional @default:0.001 -->
### `dTolerance`

- The tolerance distance for similarity test.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strSource`

- The name of the Jupiter doc to copy.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strTarget`

- The name of the Jupiter doc to paste.

## Return Code

A _Boolean_ of _True_ if success, or _False_ if fail.

## Sample Code

```psj {16,17,18}
Geometry.Part.Cube(iPartColor=12999622)
Geometry.MakeFillet(crlEdges=[Edge(18, 19, 15)])
Meshing.LocalSettings.Face(strName="MeshParam _1",
                           localMesh=LOCAL _MESH(iEntityType=2,
                                                bEnableSizeParams=True,
                                                dAvgElemSize=0.002,
                                                dMaxElemSize=0.01,
                                                dMinElemSize=0.001,
                                                bEnableMeshPattern=True,
                                                iMeshPatternType=1),
                           crlTargets=[Face(27, 28, 29)])

Geometry.Part.Cube(strName="Cube _2", iPartColor=7731705)
Geometry.MakeFillet(crlEdges=[Edge(93, 90, 94)])

copy _status = Meshing.Templates.TemplateCopy(crlReferent=[Part(1)],
                                             crlTargets=[Part(2)],
                                             dTolerance=1e-06)

JPT.Debugger(copy _status)
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
