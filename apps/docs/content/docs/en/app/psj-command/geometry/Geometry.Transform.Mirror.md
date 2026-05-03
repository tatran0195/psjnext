---
title: "Geometry.Transform.Mirror()"
description: "Mirror body"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Transform > Mirror"
macro_link: "[MirrorBody](../../macro/geometry/MirrorBody)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

This method mirrors existing part geometry across a plane to create new geometry.

## Syntax

```psj
Geometry.Transform.Mirror(crlParts, veclPoint=[[0.0, 0.0, 0.0]], dOffset=0.0, bCreateNewPart=True,
    bCopyLBC=False, bCopyProperty=False, bRemoveDupFace=True, bMergeNode=False, dTol=1e-05)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to mirror.

### `veclPoint` @type(List\[Vector]) @default(\[\[0.0, 0.0, 0.0]])

- The X-, Y-, and Z-coordinates of three-points to define the mirror plane.

### `dOffset` @type(Double) @default(0.0)

- The offset amount from the mirror plane.

### `bCreateNewPart` @type(Boolean) @default(True)

- Whether or not the mirrored part should be moved to a new part and keep the original part as is.

### `bCopyLBC` @type(Boolean) @default(False)

- Whether to copy all load boundary condition from original part to mirrored part. This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

### `bCopyProperty` @type(Boolean) @default(False)

- Whether to copy all property from original part to mirrored part. This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

### `bRemoveDupFace` @type(Boolean) @default(True)

- Whether to remove the faces which overlap the mirrored with the original part. This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

### `bMergeNode` @type(Boolean) @default(False)

- Whether to merge nodes of mirrored part and the original part are at a distance of less than or equal to the specified value.

### `dTol` @type(Double) @default(1e-05)

- The maximum distance of the coupling nodes. This argument will be ignored i&#x66;_&#x62;MergeNode=False_.

### `bCopyReference` @type(Boolean) @default(False) @since(5.1.0)

- Whether to copy references from the existing part to the created parts or not.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Wedge()

Geometry.Transform.Mirror(crlParts=[Part(1)], veclPoint=[[0.012, 0, 0], [0, 0.012, 0], [0.012, 0, 1]])
```
