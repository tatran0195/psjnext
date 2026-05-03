---
title: "Geometry.Transform.MatingFace()"
description: "Transform Mating Face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Transform > Mating Face"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Translate parts by defining mating faces, mating edges, and mating points.

## Syntax

```psj
Geometry.Transform.MatingFace(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- Parts to transform.

### `crSrcFace` @type(Cursor) @required

- The face to be used as the source for the transform operation.

### `crDstFace` @type(Cursor) @required

- The face to be used as the reference for the transform operation.

### `crSrcEdge` @type(Cursor) @default(None)

- The edge to be used as the source for the transform operation.

### `crDstEdge` @type(Cursor) @default(None)

- The edge to be used as the reference for the transform operation. This argument must be specified whe&#x6E;_&#x69;AlignMethodType=0_.

### `crSrcNode` @type(Cursor) @default(None)

- The node to be used as the source for the transform operation.

### `crDstNode` @type(Cursor) @default(None)

- The node to be used as the reference for the transform operation. This argument must be specified whe&#x6E;_&#x69;AdjustPointType=0_.

### `iFaceOpposite` @type(Integer) @default(0)

- Whether or not the source surface should be on the opposite side of the destination surface.
  - I&#x66;_&#x69;FaceOpposite=0_: The source surface lay on the current side of the destination surface.
  - I&#x66;_&#x69;FaceOpposite=1_: The source surface lay on the opposite side of the destination surface.

### `dEdgeAngle` @type(Double) @default(0.0)

- The angle in degrees between two specified edges,_crSrcEdg&#x65;_&#x61;n&#x64;_&#x63;rDstEdge_, after the transform operation.

### `iEdgeOpposite` @type(Integer) @default(0)

- Whether to match the opposite direction of source edge to destination edge.
  - I&#x66;_&#x69;EdgeOpposite=0_: Match the current direction of source edge to destination edge.
  - I&#x66;_&#x69;EdgeOpposite=1_: Match the opposite direction of source edge to destination edge.

### `iAlignMethodType` @type(Integer) @default(0)

- How to align the edges between the source and the destination. This argument will be ignored i&#x66;_&#x63;rSrcEdg&#x65;_&#x68;as a default value.
  - I&#x66;_&#x69;AlignMethodType=0_: Move the given source part so tha&#x74;_&#x63;rSrcEdg&#x65;_&#x69;s coincident wit&#x68;_&#x63;rDstEdge_.
  - I&#x66;_&#x69;AlignMethodType=1_: Mov&#x65;_&#x63;rSrcEdg&#x65;_&#x65;dges along the direction of the specified vecto&#x72;_&#x64;lAlignVector_.

### `iAdjustPointType` @type(Integer) @default(0)

- How to move the node along the direction. This argument will be ignored i&#x66;_&#x63;rSrcNod&#x65;_&#x68;as a default value.
  - I&#x66;_&#x69;AdjustPointType=0_: Move on a direction defined by two nodes, from source and destination.
  - I&#x66;_&#x69;AdjustPointType=1_: Move on a direction defined by a node and a coordinate, from source and destination.

### `iAdjustProjectionType` @type(Integer) @default(0)

- The projection direction. This argument will be ignored i&#x66;_&#x63;rSrcNod&#x65;_&#x68;as a default value.
  - I&#x66;_&#x69;AdjustProjectionType=0_: Projection direction is the normal direction of the surface.
  - I&#x66;_&#x69;AdjustProjectionType=1_: Projection direction is the specified vecto&#x72;_&#x64;lAdjustVector_.

### `dlAlignVector` @type(List\[Double]) @default(\[0.0, 0.0, 0.0])

- The alignment vector. This argument is used whe&#x6E;_&#x69;AlignMethodType=1_.

### `dlAdjustPoint` @type(List\[Double]) @default(\[0.0, 0.0, 0.0])

- The destination point whic&#x68;_&#x63;rSrcNod&#x65;_&#x77;ill move to. This argument is used whe&#x6E;_&#x69;AdjustPointType=1_.

### `dlAdjustVector` @type(List\[Double]) @default(\[0.0, 0.0, 0.0])

- Adjustment vector. This argument is used whe&#x6E;_&#x69;AdjustPointType=1_.

### `bCreateNewPart` @type(Boolean) @default(False)

- Whether to keep the original part and make a copy one then transform.

### `bCopyLBC` @type(Boolean) @default(False)

- Whether to copy load boundary condition of original part to transformed part. This argument is used whe&#x6E;_&#x62;CreateNewPart=True_.

### `bCopyProperty` @type(Boolean) @default(False)

- Whether to copy property of original part to transformed part. This argument is used whe&#x6E;_&#x62;CreateNewPart=True_.

### `bIsPreview` @type(Boolean) @default(False)

- Whether to enable preview or not.

### `crlCoordSyss` @type(List\[Cursor]) @default(\[])

- The coordinate systems.

### `bCopyReference` @type(Boolean) @default(False) @since(5.1.0)

- Whether to copy references from the existing part to the created parts or not.

## Return Code

No return value.

## Sample Code

```psj {3}
Geometry.Part.Cube()
Geometry.Part.Cylinder(dlOrigin=[0.02, 0.005, 0.005], dTopOuterRadius=0.005, dBottomOuterRadius=0.005)
Geometry.Transform.MatingFace(crlParts=[Part(2)], crSrcFace=Face(30), crDstFace=Face(22))
```
