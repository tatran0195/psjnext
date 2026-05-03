---
title: "Geometry.StitchEdge()"
description: "Stitch Edges"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Stitch Edge"
macro_link: "[StitchEdge](../../macro/geometry/StitchEdge)"
---

## Description

This method stitches any gap between free edges that are slightly apart.

## Syntax

```psj
Geometry.StitchEdge(crlMaster, crlSlave, dTolerance=0.3, bKeepSlave=True)
```

## Inputs

### `crlMaster` @type(List\[Cursor]) @required

- Master edges will be retained after operation.

### `crlSlave` @type(List\[Cursor]) @required

- Slave edges to be stitched.

### `dTolerance` @type(Double) @default(0.3)

- The stitch tolerance. The free edges are at a distance less than or equal to the specified value will be stitched.

### `bKeepSlave` @type(Boolean) @default(True)

- Whether to keep slave nodes after the stitch operation.

## Return Code

A _String_ of 1 if success, or 0 if fail.

## Sample Code

```psj
Geometry.Part.Cube()

Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], ilNodeCnt=[10, 10, 11], strName="Cube_2")

Geometry.StitchEdge(crlMaster=[Edge(15)], crlSlave=[Edge(39))
```
