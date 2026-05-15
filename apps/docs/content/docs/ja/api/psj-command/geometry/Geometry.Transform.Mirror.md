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

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the parts to mirror.

<!-- @since:5.0.1 @optional -->
### veclPoint

- Specify the X-, Y-, and Z-coordinates of three-points to define the mirror plane.
- The default value is \[\[0.0, 0.0, 0.0]].

<!-- @since:5.0.1 @optional -->
### dOffset

- Specify the offset amount from the mirror plane.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### bCreateNewPart

- Specify whether or not the mirrored part should be moved to a new part and keep the original part as is.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bCopyLBC

- Specify whether to copy all load boundary condition from original part to mirrored part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyProperty

- Specify whether to copy all property from original part to mirrored part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bRemoveDupFace

- Specify whether to remove the faces which overlap the mirrored with the original part. This argument will be ignored if _bCreateNewPart=False_.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### bMergeNode

- Specify whether to merge nodes of mirrored part and the original part are at a distance of less than or equal to the specified value.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the maximum distance of the coupling nodes. This argument will be ignored if _bMergeNode=False_.
- The default value is 1e-05.

<!-- @since:5.1.0 @optional -->
### bCopyReference

- Specify whether to copy references from the existing part to the created parts or not.
- The default value is _False_.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Wedge()

Geometry.Transform.Mirror(crlParts=[Part(1)], veclPoint=[[0.012, 0, 0], [0, 0.012, 0], [0.012, 0, 1]])
```
