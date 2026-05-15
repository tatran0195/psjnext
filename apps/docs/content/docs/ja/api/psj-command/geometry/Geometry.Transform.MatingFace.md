---
title: "Geometry.Transform.MatingFace()"
description: "Transform Mating Face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Transform > Mating Face"
---

## Description

Translate parts by defining mating faces, mating edges, and mating points.

## Syntax

```psj
Geometry.Transform.MatingFace(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify parts to transform.

<!-- @since:5.0.1 @required -->
### crSrcFace

- Specify the face to be used as the source for the transform operation.

<!-- @since:5.0.1 @required -->
### crDstFace

- Specify the face to be used as the reference for the transform operation.

<!-- @since:5.0.1 @optional -->
### crSrcEdge

- Specify the edge to be used as the source for the transform operation.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crDstEdge

- Specify the edge to be used as the reference for the transform operation. This argument must be specified when _iAlignMethodType=0_.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crSrcNode

- Specify the node to be used as the source for the transform operation.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crDstNode

- Specify the node to be used as the reference for the transform operation. This argument must be specified when _iAdjustPointType=0_.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iFaceOpposite

- Specify whether or not the source surface should be on the opposite side of the destination surface.
  - If _iFaceOpposite=0_: The source surface lay on the current side of the destination surface.
  - If _iFaceOpposite=1_: The source surface lay on the opposite side of the destination surface.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dEdgeAngle

- Specify the angle in degrees between two specified edges,_crSrcEdge_ and _crDstEdge_, after the transform operation.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iEdgeOpposite

- Specify whether to match the opposite direction of source edge to destination edge.
  - If _iEdgeOpposite=0_: Match the current direction of source edge to destination edge.
  - If _iEdgeOpposite=1_: Match the opposite direction of source edge to destination edge.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAlignMethodType

- Specify how to align the edges between the source and the destination. This argument will be ignored if _crSrcEdge_ has a default value.
  - If _iAlignMethodType=0_: Move the given source part so that _crSrcEdge_ is coincident with _crDstEdge_.
  - If _iAlignMethodType=1_: Move _crSrcEdge_ edges along the direction of the specified vector _dlAlignVector_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAdjustPointType

- Specify how to move the node along the direction. This argument will be ignored if _crSrcNode_ has a default value.
  - If _iAdjustPointType=0_: Move on a direction defined by two nodes, from source and destination.
  - If _iAdjustPointType=1_: Move on a direction defined by a node and a coordinate, from source and destination.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAdjustProjectionType

- Specify the projection direction. This argument will be ignored if _crSrcNode_ has a default value.
  - If _iAdjustProjectionType=0_: Projection direction is the normal direction of the surface.
  - If _iAdjustProjectionType=1_: Projection direction is the specified vector _dlAdjustVector_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dlAlignVector

- Specify the alignment vector. This argument is used when _iAlignMethodType=1_.
- The default value is \[0.0, 0.0, 0.0].

<!-- @since:5.0.1 @optional -->
### dlAdjustPoint

- Specify the destination point which _crSrcNode_ will move to. This argument is used when _iAdjustPointType=1_.
- The default value is \[0.0, 0.0, 0.0].

<!-- @since:5.0.1 @optional -->
### dlAdjustVector

- Specify adjustment vector. This argument is used when _iAdjustPointType=1_.
- The default value is \[0.0, 0.0, 0.0].

<!-- @since:5.0.1 @optional -->
### bCreateNewPart

- Specify whether to keep the original part and make a copy one then transform.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyLBC

- Specify whether to copy load boundary condition of original part to transformed part. This argument is used when _bCreateNewPart=True_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyProperty

- Specify whether to copy property of original part to transformed part. This argument is used when _bCreateNewPart=True_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bIsPreview

- Specify whether to enable preview or not.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crlCoordSyss

- Specify the coordinate systems.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### bCopyReference

- Specify whether to copy references from the existing part to the created parts or not.
- The default value is _False_.

## Return Code

No return value.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Geometry.Part.Cylinder(dlOrigin=[0.02, 0.005, 0.005], dTopOuterRadius=0.005, dBottomOuterRadius=0.005)
Geometry.Transform.MatingFace(crlParts=[Part(2)], crSrcFace=Face(30), crDstFace=Face(22))
```
