---
title: "Test.ZGeometryTest.IntersectionCheck()"
description: "Intersection check"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Test > ZGeometryTest > IntersectionCheck"
---

## Description

Intersection check

## Syntax

```psj
Test.ZGeometryTest.IntersectionCheck(crlParts, crlFaces, crlElems, iType)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The part.

### `crlFaces` @type(List\[Cursor]) @required

- The face.

### `crlElems` @type(List\[Cursor]) @required

- The element.

### `iType` @type(Integer) @required

- The type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.ZGeometryTest.IntersectionCheck(crlParts, crlFaces, crlElems, iType)
```
