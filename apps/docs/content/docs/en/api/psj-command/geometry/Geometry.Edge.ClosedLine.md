---
title: "Geometry.Edge.ClosedLine()"
description: "Imprint closed lines onto face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Edge > Closed Line"
macro _link: "[ImprintCloseLineS](../../macro/geometry/ImprintCloseLineS)"
---

## Description

This method imprints closed lines onto the given face.

## Syntax

```psj
Geometry.Edge.ClosedLine(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Vector] @required -->
<!-- @since:5.1.0 @type:List[Position] -->
### `veclPositions`

- The points on the target faces.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargetFace`

- The target faces on which the edges are imprinted.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bBreakFace`

- Whether to break the given faces where possible.

<!-- @since:5.0.1 @type:List[Cursor] @removed:5.1.0 @required @deprecated -->
### `crlTargetsFace`

- The faces to be imprinted.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iEnableBreakFace`

- Whether to break the given faces after the imprint operation. Possible values are 0 and 1.
- If _iEnableBreakFace=0_, do not break given face where possible after the imprint operation.
- If _iEnableBreakFace=1_, break given face where possible after the imprint operation.

## Return Code

A _List of Cursor_ specifying the new created edges.

## Sample Code

```psj {3-7}
Geometry.Part.Cube()

closed _lines = Geometry.Edge.ClosedLine(veclPositions=[[0.0058, 0.0028, 0.01], 
                                        [0.0038, 0.0029, 0.01], 
                                        [0.0040, 0.0047, 0.01], 
                                        [0.0063, 0.0046, 0.01]],
                                         crlTargetsFace=[Face(26)])
JPT.Debugger(closed _lines)
```
