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

<!-- @since:5.0.1 @optional -->
### bIType

- Specify the type.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### crExtFace

- Specify the extend face.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crRefFace

- Specify the reference face.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crEdge

- Specify the edge.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iFaceType

- Specify the face type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iExtendType

- Specify the extend type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dParaZxy

- Specify the parameter zxy.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAxisPlane

- Specify the axis plane.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iParaArcNodesNum

- Specify the parameter arc nodes number.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dOffLength

- Specify the off length.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dCoMag

- Specify the coordinate mag.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAxisSystem

- Specify the axis system.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCoorSystem

- Specify the coordinate system.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iCoX

- Specify the coordinate x.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCoY

- Specify the coordinate y.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCoZ

- Specify the coordinate z.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bOtherSameAsFaceNormal

- Specify the other same as face normal.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### dOtherArcNodesNum

- Specify the other arc nodes number.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dOtherArcRadius

- Specify the other arc radius.
- The default value is 0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.ExtendFace.PlanarFace(bIType=False, crExtFace=None, crRefFace=None, crEdge=None, iFaceType=0, iExtendType=0, iMethod=0, dParaZxy=0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0, dCoMag=0, iAxisSystem=0, iCoorSystem=0, crCoord=None, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0, dOtherArcRadius=0)
```
