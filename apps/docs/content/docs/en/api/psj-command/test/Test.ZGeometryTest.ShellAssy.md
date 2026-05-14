---
title: "Test.ZGeometryTest.ShellAssy()"
description: "Unknown Description"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Test > ZGeometryTest > ShellAssy"
---

## Description

Unknown Description

## Syntax

```psj
Test.ZGeometryTest.ShellAssy(taPart=[], crlFaces=[], _iMeshType=0, _bSelfIntersection=False, _iMethod=3, _dGapTol=2.1)
```

## Inputs

<!-- @since:5.0.1 @type:TA _PART @optional @default:[] -->
### `taPart`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The face.

### `_iMeshType`

- A \__I\_MESH\_TYPE_ specifying the mesh type.

### `_bSelfIntersection`

- A \__B\_SELF\_INTERSECTION_ specifying the self intersection.

### `_iMethod`

- A \__I\_METHOD_ specifying the method.

### `_dGapTol`

- A \__D\_GAP\_TOL_ specifying the gap tolerance.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.ZGeometryTest.ShellAssy(taPart=[], crlFaces=[], _iMeshType=0, _bSelfIntersection=False, _iMethod=3, _dGapTol=2.1)
```
