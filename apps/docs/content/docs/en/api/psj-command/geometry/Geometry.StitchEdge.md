---
title: "Geometry.StitchEdge()"
description: "Stitch Edges"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Stitch Edge"
macro _link: "[StitchEdge](../../macro/geometry/StitchEdge)"
---

## Description

This method stitches any gap between free edges that are slightly apart.

## Syntax

```psj
Geometry.StitchEdge(crlMaster, crlSlave, dTolerance=0.3, bKeepSlave=True)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlMaster`

- The master edges will be retained after operation.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlSlave`

- The slave edges to be stitched.

<!-- @since:5.0.1 @type:Double @optional @default:0.3 -->
### `dTolerance`

- The stitch tolerance. The free edges are at a distance less than or equal to the specified value will be stitched.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bKeepSlave`

- Whether to keep slave nodes after the stitch operation.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], ilNodeCnt=[10, 10, 11], strName="Cube _2")

Geometry.StitchEdge(crlMaster=[Edge(15)], crlSlave=[Edge(39))
```
