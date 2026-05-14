---
title: "Geometry.Transform.Mirror()"
description: "Mirror body"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Transform > Mirror"
macro _link: "[MirrorBody](../../macro/geometry/MirrorBody)"
---

## Description

This method mirrors existing part geometry across a plane to create new geometry.

## Syntax

```psj
Geometry.Transform.Mirror(crlParts, veclPoint=[[0.0, 0.0, 0.0]], dOffset=0.0, bCreateNewPart=True,
    bCopyLBC=False, bCopyProperty=False, bRemoveDupFace=True, bMergeNode=False, dTol=1e-05)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts to mirror.

<!-- @since:5.0.1 @type:List[Vector] @optional @default:[[0.0, 0.0, 0.0]] -->
### `veclPoint`

- The X-, Y-, and Z-coordinates of three-points to define the mirror plane.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dOffset`

- The offset amount from the mirror plane.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bCreateNewPart`

- Whether or not the mirrored part should be moved to a new part and keep the original part as is.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyLBC`

- Whether to copy all load boundary condition from original part to mirrored part. This argument will be ignored if _bCreateNewPart=False_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyProperty`

- Whether to copy all property from original part to mirrored part. This argument will be ignored if _bCreateNewPart=False_.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bRemoveDupFace`

- Whether to remove the faces which overlap the mirrored with the original part. This argument will be ignored if _bCreateNewPart=False_.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMergeNode`

- Whether to merge nodes of mirrored part and the original part are at a distance of less than or equal to the specified value.

<!-- @since:5.0.1 @type:Double @optional @default:1e-05 -->
### `dTol`

- The maximum distance of the coupling nodes. This argument will be ignored if _bMergeNode=False_.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCopyReference`

- Whether to copy references from the existing part to the created parts or not.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Wedge()

Geometry.Transform.Mirror(crlParts=[Part(1)], veclPoint=[[0.012, 0, 0], [0, 0.012, 0], [0.012, 0, 1]])
```
