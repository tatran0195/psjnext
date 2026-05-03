---
title: "MidPlaneEdit.ExtendFace.CylinderFace()"
description: "project an edge to face to get a new edge"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "MidPlaneEdit > ExtendFace > CylinderFace"
---

## Description

Project an edge to face to get a new edge

## Syntax

```psj
MidPlaneEdit.ExtendFace.CylinderFace(crlExtFace=[], crRefFace=None, crEdge=None, iExtendType=1, iFaceType=0, iMethod=0, dParaAngleOffset=0.0, dParaArcLength=0.0, dParaZxy=0.0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0.0, crlSelExtendedFace=[], crlSelRefFace=[], dCoMag=0.0, iAxisSystem=0, iCoorSystem=0, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0.0, dOtherArcRadius=0.0)
```

## Inputs

### `crlExtFace` @type(List\[Cursor]) @default(\[])

- The extend face.

### `crRefFace` @type(Cursor) @default(None)

- The reference face.

### `crEdge` @type(Cursor) @default(None)

- The edge.

### `iExtendType` @type(Integer) @default(1)

- The extend type.

### `iFaceType` @type(Integer) @default(0)

- The face type.

### `iMethod` @type(Integer) @default(0)

- The method.

### `dParaAngleOffset` @type(Double) @default(0.0)

- The parameter angle offset.

### `dParaArcLength` @type(Double) @default(0.0)

- The parameter arc length.

### `dParaZxy` @type(Double) @default(0.0)

- The parameter zxy.

### `iAxisPlane` @type(Integer) @default(0)

- The axis plane.

### `iParaArcNodesNum` @type(Integer) @default(0)

- The parameter arc nodes number.

### `dOffLength` @type(Double) @default(0.0)

- The off length.

### `crlSelExtendedFace` @type(List\[Cursor]) @default(\[])

- The selection extended face.

### `crlSelRefFace` @type(List\[Cursor]) @default(\[])

- The selection reference face.

### `dCoMag` @type(Double) @default(0.0)

- The coordinate mag.

### `iAxisSystem` @type(Integer) @default(0)

- The axis system.

### `iCoorSystem` @type(Integer) @default(0)

- The coordinate system.

### `iCoX` @type(Integer) @default(0)

- The coordinate x.

### `iCoY` @type(Integer) @default(0)

- The coordinate y.

### `iCoZ` @type(Integer) @default(0)

- The coordinate z.

### `bOtherSameAsFaceNormal` @type(Boolean) @default(False)

- The other same as face normal.

### `dOtherArcNodesNum` @type(Double) @default(0.0)

- The other arc nodes number.

### `dOtherArcRadius` @type(Double) @default(0.0)

- The other arc radius.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
MidPlaneEdit.ExtendFace.CylinderFace(crlExtFace=[], crRefFace=None, crEdge=None, iExtendType=1, iFaceType=0, iMethod=0, dParaAngleOffset=0.0, dParaArcLength=0.0, dParaZxy=0.0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0.0, crlSelExtendedFace=[], crlSelRefFace=[], dCoMag=0.0, iAxisSystem=0, iCoorSystem=0, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0.0, dOtherArcRadius=0.0)
```
