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

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the part.

<!-- @since:5.0.1 @required -->
### crlFaces

- Specify the face.

<!-- @since:5.0.1 @required -->
### crlElems

- Specify the element.

<!-- @since:5.0.1 @required -->
### iType

- Specify the type.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Test.ZGeometryTest.IntersectionCheck(crlParts, crlFaces, crlElems, iType)
```
