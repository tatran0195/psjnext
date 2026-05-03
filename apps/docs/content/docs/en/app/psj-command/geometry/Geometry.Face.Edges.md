---
title: "Geometry.Face.Edges()"
description: "Create a face using the given edges as the face's boundaries. It will create a face by creating the geometry consisting of the underlying surface, associated edges, and vertices. The planar surfaces and smooth surfaces are switched by changing the related arguments"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Face > Edges"
macro_link: "[CreateFaceFromEdges](../../macro/geometry/CreateFaceFromEdges)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create a face using the given edges as the face's boundaries. It will create a face by creating the geometry consisting of the underlying surface, associated edges, and vertices. The planar surfaces and smooth surfaces are switched by changing the related arguments.

## Syntax

```psj
Geometry.Face.Edges(...)
```

## Inputs

### `crlEdges` @type(List\[Cursor])

- The edges that bound the new face. Eithe&#x72;_&#x63;rlEdge&#x73;_&#x6F;&#x72;_&#x63;rlNode&#x73;_&#x6D;ust be specified.

### `crlParts` @type(List\[Cursor]) @default(\[])

- A given part to that the new face will belong.

### `crlNodes` @type(List\[Cursor]) @default(\[])

- Two nodes to define the direction in which the curved surface be created smoothly. I&#x66;_&#x63;rlNode&#x73;_&#x69;s specified, the curved surface will be smoother than the face created by bound edges only.

### `bSharedFace` @type(Boolean) @default(False)

- Whether to create a shared face when the given edges are shared edges.

### `bSmoothFace` @type(Boolean) @default(False)

- Whether to create a smooth face instead of planar face.

### `bCreatePart` @type(Boolean) @default(False)

- Whether to stitch the newly created face to the new part. I&#x66;_&#x62;SharedFace=True_, this argument will be ignored.

### `bImproved` @type(Boolean) @default(False)

- Whether the newly created face is created with smooth direction. This argument does not affect the operation i&#x66;_&#x63;rlNode&#x73;_&#x69;s not specified.

### `bBarsOnly` @type(Boolean) @default(False)

- Indicating whether all of the selected edges are Bar part only.

### `bOnlyOnePart` @type(Boolean) @default(True)

- Indicating whether the newly created face is in the same new part. I&#x66;_&#x62;CreatePart=False_, this argument will be ignored.

### `bIncludeMidNodes` @type(Boolean) @default(False)

- Whether to include middle nodes when creating face.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {3}
Geometry.Part.Cube()

created_face = Geometry.Face.Edges(crlEdges=[Edge(9, 19)])

JPT.Debugger(created_face)
```
