---
title: "Geometry.SquareUpFillet()"
description: "Square Up Fillet"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Square Up Fillet"
macro _link: "[SquareUpFillet](../../macro/geometry/SquareUpFillet)"
---

## Description

This method turns fillet parts into rectangular angles.

## Syntax

```psj
Geometry.SquareUpFillet(crlFaces)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlFaces`

- The fillet faces to square up.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.MakeFillet(crlEdges=[Edge(19)])

Geometry.SquareUpFillet(crlFaces=[Face(27)])
```
