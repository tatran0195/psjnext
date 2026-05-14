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

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlEdges`

- The edges that bound the new face. Either _crlEdges_ or _crlNodes_ must be specified.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- A given part to that the new face will belong.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The two nodes to define the direction in which the curved surface be created smoothly. If _crlNodes_ is specified, the curved surface will be smoother than the face created by bound edges only.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSharedFace`

- Whether to create a shared face when the given edges are shared edges.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSmoothFace`

- Whether to create a smooth face instead of planar face.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCreatePart`

- Whether to stitch the newly created face to the new part. If _bSharedFace=True_, this argument will be ignored.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bImproved`

- Whether the newly created face is created with smooth direction. This argument does not affect the operation if _crlNodes_ is not specified.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bBarsOnly`

- The indicating whether all of the selected edges are Bar part only.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bOnlyOnePart`

- The indicating whether the newly created face is in the same new part. If _bCreatePart=False_, this argument will be ignored.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bIncludeMidNodes`

- Whether to include middle nodes when creating face.

## Return Code

A _Cursor_ specifying the new created face.

## Sample Code

```psj {3}
Geometry.Part.Cube()

created _face = Geometry.Face.Edges(crlEdges=[Edge(9, 19)])

JPT.Debugger(created _face)
```
