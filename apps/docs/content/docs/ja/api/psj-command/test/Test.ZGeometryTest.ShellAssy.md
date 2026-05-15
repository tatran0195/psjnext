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

<!-- @since:5.0.1 @optional -->
### taPart

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the face.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### \_iMeshType

- Specify the mesh type.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### \_bSelfIntersection

- Specify the self intersection.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### \_iMethod

- Specify the method.
- The default value is 3.

<!-- @since:5.0.1 @optional -->
### \_dGapTol

- Specify the gap tolerance.
- The default value is 2.1.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.ZGeometryTest.ShellAssy(taPart=[], crlFaces=[], _iMeshType=0, _bSelfIntersection=False, _iMethod=3, _dGapTol=2.1)
```
