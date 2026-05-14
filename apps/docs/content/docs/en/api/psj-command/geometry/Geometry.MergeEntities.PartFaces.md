---
title: "Geometry.MergeEntities.PartFaces()"
description: "Merge Faces in Part"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Merge Entities > Part Faces"
---

## Description

This method merges adjacent faces of the given part by recursively finding adjacent faces that are at an angle of less than or equal to the specified angle or face width is not greater than the specified value. The operation will ignore the specified preserved faces.

## Syntax

```psj
Geometry.MergeEntities.PartFaces(crlParts=[], crlFaces=[], bAngle=True, dTolAngle=20, bWidth=True,
    dTolWidth=0.2)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The target parts that faces need merging belong to.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The preserved faces not to be merged.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bAngle`

- Whether to find the adjacent faces by face angle.

<!-- @since:5.0.1 @type:Double @optional @default:20.0 -->
### `dTolAngle`

- The maximum allowable angle between two adjacent faces. If _bAngle_ is specified, the adjacent faces that are at an angle of less than or equal to will be merged.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bWidth`

- Whether to find the adjacent faces by face width.

<!-- @since:5.0.1 @type:Double @optional @default:0.2 -->
### `dTolWidth`

- The maximum allowable face width. If _bWidth_ is specified, the faces that have a width less than or equal to will be merged to an adjacent face.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Trapezoid(dTopXLength=5.0)

Geometry.MergeEntities.PartFaces(crlParts=[Part(1)], dTolAngle=89.0, bWidth=False)
```
