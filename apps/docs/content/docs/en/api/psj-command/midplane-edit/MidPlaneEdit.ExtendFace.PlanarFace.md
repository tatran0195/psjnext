---
title: "MidPlaneEdit.ExtendFace.PlanarFace()"
description: "Extend Face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MidPlaneEdit > ExtendFace > PlanarFace"
---

## Description

Extend Face

## Syntax

```psj
MidPlaneEdit.ExtendFace.PlanarFace(bIType=False, crExtFace=None, crRefFace=None, crEdge=None, iFaceType=0, iExtendType=0, iMethod=0, dParaZxy=0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0, dCoMag=0, iAxisSystem=0, iCoorSystem=0, crCoord=None, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0, dOtherArcRadius=0)
```

## Inputs

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIType`

- The type.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crExtFace`

- The extend face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crRefFace`

- The reference face.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdge`

- The edge.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFaceType`

- The face type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iExtendType`

- The extend type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dParaZxy`

- The parameter zxy.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAxisPlane`

- The axis plane.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iParaArcNodesNum`

- The parameter arc nodes number.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dOffLength`

- The off length.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dCoMag`

- The coordinate mag.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAxisSystem`

- The axis system.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iCoorSystem`

- The coordinate system.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

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

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dOtherArcNodesNum`

- The other arc nodes number.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dOtherArcRadius`

- The other arc radius.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.ExtendFace.PlanarFace(bIType=False, crExtFace=None, crRefFace=None, crEdge=None, iFaceType=0, iExtendType=0, iMethod=0, dParaZxy=0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0, dCoMag=0, iAxisSystem=0, iCoorSystem=0, crCoord=None, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0, dOtherArcRadius=0)
```
