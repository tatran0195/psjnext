---
title: "MidPlaneEdit.ExtendFace.PlanarFace()"
description: "Extend Face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > ExtendFace > PlanarFace"
---

## Description

Extend Face

## Syntax

```psj
MidPlaneEdit.ExtendFace.PlanarFace(bIType=False, crExtFace=None, crRefFace=None, crEdge=None, iFaceType=0, iExtendType=0, iMethod=0, dParaZxy=0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0, dCoMag=0, iAxisSystem=0, iCoorSystem=0, crCoord=None, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0, dOtherArcRadius=0)
```

## Inputs

### `bIType` @type(Boolean) @default(False)

- The type.

### `crExtFace` @type(Cursor) @default(None)

- The extend face.

### `crRefFace` @type(Cursor) @default(None)

- The reference face.

### `crEdge` @type(Cursor) @default(None)

- The edge.

### `iFaceType` @type(Integer) @default(0)

- The face type.

### `iExtendType` @type(Integer) @default(0)

- The extend type.

### `iMethod` @type(Integer) @default(0)

- The method.

### `dParaZxy` @type(Double) @default(0)

- The parameter zxy.

### `iAxisPlane` @type(Integer) @default(0)

- The axis plane.

### `iParaArcNodesNum` @type(Integer) @default(0)

- The parameter arc nodes number.

### `dOffLength` @type(Double) @default(0)

- The off length.

### `dCoMag` @type(Double) @default(0)

- The coordinate mag.

### `iAxisSystem` @type(Integer) @default(0)

- The axis system.

### `iCoorSystem` @type(Integer) @default(0)

- The coordinate system.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `iCoX` @type(Integer) @default(0)

- The coordinate x.

### `iCoY` @type(Integer) @default(0)

- The coordinate y.

### `iCoZ` @type(Integer) @default(0)

- The coordinate z.

### `bOtherSameAsFaceNormal` @type(Boolean) @default(False)

- The other same as face normal.

### `dOtherArcNodesNum` @type(Double) @default(0)

- The other arc nodes number.

### `dOtherArcRadius` @type(Double) @default(0)

- The other arc radius.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.ExtendFace.PlanarFace(bIType=False, crExtFace=None, crRefFace=None, crEdge=None, iFaceType=0, iExtendType=0, iMethod=0, dParaZxy=0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0, dCoMag=0, iAxisSystem=0, iCoorSystem=0, crCoord=None, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0, dOtherArcRadius=0)
```
