---
title: "MidPlaneEdit.ExtendFace.CylinderFace()"
description: "project an edge to face to get a new edge"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > ExtendFace > CylinderFace"
---

## Description

Project an edge to face to get a new edge

## Syntax

```psj
MidPlaneEdit.ExtendFace.CylinderFace(crlExtFace=[], crRefFace=None, crEdge=None, iExtendType=1, iFaceType=0, iMethod=0, dParaAngleOffset=0.0, dParaArcLength=0.0, dParaZxy=0.0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0.0, crlSelExtendedFace=[], crlSelRefFace=[], dCoMag=0.0, iAxisSystem=0, iCoorSystem=0, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0.0, dOtherArcRadius=0.0)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlExtFace`

- The extend face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crRefFace`

- The reference face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdge`

- The edge.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iExtendType`

- The extend type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFaceType`

- The face type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dParaAngleOffset`

- The parameter angle offset.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dParaArcLength`

- The parameter arc length.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dParaZxy`

- The parameter zxy.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAxisPlane`

- The axis plane.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iParaArcNodesNum`

- The parameter arc nodes number.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dOffLength`

- The off length.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSelExtendedFace`

- The selection extended face.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSelRefFace`

- The selection reference face.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dCoMag`

- The coordinate mag.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAxisSystem`

- The axis system.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoorSystem`

- The coordinate system.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoX`

- The coordinate x.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoY`

- The coordinate y.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoZ`

- The coordinate z.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bOtherSameAsFaceNormal`

- The other same as face normal.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dOtherArcNodesNum`

- The other arc nodes number.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dOtherArcRadius`

- The other arc radius.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.ExtendFace.CylinderFace(crlExtFace=[], crRefFace=None, crEdge=None, iExtendType=1, iFaceType=0, iMethod=0, dParaAngleOffset=0.0, dParaArcLength=0.0, dParaZxy=0.0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0.0, crlSelExtendedFace=[], crlSelRefFace=[], dCoMag=0.0, iAxisSystem=0, iCoorSystem=0, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0.0, dOtherArcRadius=0.0)
```
