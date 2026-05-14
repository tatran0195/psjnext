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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts to transform.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crSrcFace`

- The face to be used as the source for the transform operation.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crDstFace`

- The face to be used as the reference for the transform operation.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSrcEdge`

- The edge to be used as the source for the transform operation.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crDstEdge`

- The edge to be used as the reference for the transform operation. This argument must be specified when _iAlignMethodType=0_.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSrcNode`

- The node to be used as the source for the transform operation.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crDstNode`

- The node to be used as the reference for the transform operation. This argument must be specified when _iAdjustPointType=0_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFaceOpposite`

- Whether or not the source surface should be on the opposite side of the destination surface.
  - If _iFaceOpposite=0_: The source surface lay on the current side of the destination surface.
  - If _iFaceOpposite=1_: The source surface lay on the opposite side of the destination surface.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dEdgeAngle`

- The angle in degrees between two specified edges,_crSrcEdge_ and _crDstEdge_, after the transform operation.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEdgeOpposite`

- Whether to match the opposite direction of source edge to destination edge.
  - If _iEdgeOpposite=0_: Match the current direction of source edge to destination edge.
  - If _iEdgeOpposite=1_: Match the opposite direction of source edge to destination edge.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAlignMethodType`

- The how to align the edges between the source and the destination. This argument will be ignored if _crSrcEdge_ has a default value.
  - If _iAlignMethodType=0_: Move the given source part so that _crSrcEdge_ is coincident with _crDstEdge_.
  - If _iAlignMethodType=1_: Move _crSrcEdge_ edges along the direction of the specified vector _dlAlignVector_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdjustPointType`

- The how to move the node along the direction. This argument will be ignored if _crSrcNode_ has a default value.
  - If _iAdjustPointType=0_: Move on a direction defined by two nodes, from source and destination.
  - If _iAdjustPointType=1_: Move on a direction defined by a node and a coordinate, from source and destination.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAdjustProjectionType`

- The projection direction. This argument will be ignored if _crSrcNode_ has a default value.
  - If _iAdjustProjectionType=0_: Projection direction is the normal direction of the surface.
  - If _iAdjustProjectionType=1_: Projection direction is the specified vector _dlAdjustVector_.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0, 0.0, 0.0] -->
### `dlAlignVector`

- The alignment vector. This argument is used when _iAlignMethodType=1_.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0, 0.0, 0.0] -->
### `dlAdjustPoint`

- The destination point which _crSrcNode_ will move to. This argument is used when _iAdjustPointType=1_.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0, 0.0, 0.0] -->
### `dlAdjustVector`

- The adjustment vector. This argument is used when _iAdjustPointType=1_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCreateNewPart`

- Whether to keep the original part and make a copy one then transform.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyLBC`

- Whether to copy load boundary condition of original part to transformed part. This argument is used when _bCreateNewPart=True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyProperty`

- Whether to copy property of original part to transformed part. This argument is used when _bCreateNewPart=True_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIsPreview`

- Whether to enable preview or not.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlCoordSyss`

- The coordinate systems.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCopyReference`

- Whether to copy references from the existing part to the created parts or not.

## Return Code

No return value.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Geometry.Part.Cylinder(dlOrigin=[0.02, 0.005, 0.005], dTopOuterRadius=0.005, dBottomOuterRadius=0.005)
Geometry.Transform.MatingFace(crlParts=[Part(2)], crSrcFace=Face(30), crDstFace=Face(22))
```
