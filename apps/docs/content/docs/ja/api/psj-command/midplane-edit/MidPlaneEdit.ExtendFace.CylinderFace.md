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

<!-- @since:5.0.1 @optional -->
### crlExtFace

- Specify the extend face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crRefFace

- Specify the reference face.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### crEdge

- Specify the edge.
- The default value is None.

<!-- @since:5.0.1 @optional -->
### iExtendType

- Specify the extend type.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iFaceType

- Specify the face type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the method.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dParaAngleOffset

- Specify the parameter angle offset.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dParaArcLength

- Specify the parameter arc length.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dParaZxy

- Specify the parameter zxy.
- The default value is 0.0.

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
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### crlSelExtendedFace

- Specify the selection extended face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSelRefFace

- Specify the selection reference face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dCoMag

- Specify the coordinate mag.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iAxisSystem

- Specify the axis system.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iCoorSystem

- Specify the coordinate system.
- The default value is 0.

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
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dOtherArcRadius

- Specify the other arc radius.
- The default value is 0.0.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.ExtendFace.CylinderFace(crlExtFace=[], crRefFace=None, crEdge=None, iExtendType=1, iFaceType=0, iMethod=0, dParaAngleOffset=0.0, dParaArcLength=0.0, dParaZxy=0.0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0.0, crlSelExtendedFace=[], crlSelRefFace=[], dCoMag=0.0, iAxisSystem=0, iCoorSystem=0, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0.0, dOtherArcRadius=0.0)
```
