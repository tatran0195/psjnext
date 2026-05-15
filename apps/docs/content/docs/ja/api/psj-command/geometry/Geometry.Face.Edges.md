---
title: "Geometry.Face.Edges()"
description: "Create a face using the given edges as the face's boundaries. It will create a face by creating the geometry consisting of the underlying surface, associated edges, and vertices. The planar surfaces and smooth surfaces are switched by changing the related arguments"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Face > Edges"
macro _link: "[CreateFaceFromEdges](../../macro/geometry/CreateFaceFromEdges)"
---

## Description

Create a face using the given edges as the face's boundaries. It will create a face by creating the geometry consisting of the underlying surface, associated edges, and vertices. The planar surfaces and smooth surfaces are switched by changing the related arguments.

## Syntax

```psj
Geometry.Face.Edges(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlEdges

- Specify the edges that bound the new face. Either _crlEdges_ or _crlNodes_ must be specified.

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify a given part to that the new face will belong.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlNodes

- Specify two nodes to define the direction in which the curved surface be created smoothly. If _crlNodes_ is specified, the curved surface will be smoother than the face created by bound edges only.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### bSharedFace

- Specify whether to create a shared face when the given edges are shared edges.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bSmoothFace

- Specify whether to create a smooth face instead of planar face.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCreatePart

- Specify whether to stitch the newly created face to the new part. If _bSharedFace=True_, this argument will be ignored.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bImproved

- Specify whether the newly created face is created with smooth direction. This argument does not affect the operation if _crlNodes_ is not specified.
- The default value is _False_.

### `bBarsOnly`

- A _Boolean_ indicating whether all of the selected edges are Bar part only.
- The default value is _False_.

### `bOnlyOnePart`

- A _Boolean_ indicating whether the newly created face is in the same new part. If _bCreatePart=False_, this argument will be ignored.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bIncludeMidNodes

- Specify whether to include middle nodes when creating face.
- The default value is _False_.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {3}
Geometry.Part.Cube()

created _face = Geometry.Face.Edges(crlEdges=[Edge(9, 19)])

JPT.Debugger(created _face)
```
