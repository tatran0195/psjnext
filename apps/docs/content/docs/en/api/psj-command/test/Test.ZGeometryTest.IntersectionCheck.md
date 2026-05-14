---
title: "Test.ZGeometryTest.IntersectionCheck()"
description: "Intersection check"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Test > ZGeometryTest > IntersectionCheck"
---

## Description

Intersection check

## Syntax

```psj
Test.ZGeometryTest.IntersectionCheck(crlParts, crlFaces, crlElems, iType)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The part.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The face.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlElems`

- The element.

<!-- @since:5.0.1 @type:Integer @required -->
### `iType`

- The type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.ZGeometryTest.IntersectionCheck(crlParts, crlFaces, crlElems, iType)
```
