---
title: "Assemble.AddRibEx.General()"
description: "Add rib part on a part."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Assemble > AddRibEx > General"
macro_link: "AddRibGeneralEx"
---

## Description

Add rib part on a part.

## Syntax

```psj
Assemble.AddRibEx.General(...)
```

## Inputs

### `dlPositions` @type(List\[Double]) @required

- Position of first end of the rib to create.

### `crlFaces` @type(List\[Cursor]) @required

- Position of second end of the rib to create.

### `dThickness` @type(Double) @default(0.0005)

- The width of the rib.

### `#dHeight` @type(Double) @default(0.001)

- The height of the rib from the attachment surface.

### `#crCoordinate` @type(Cursor) @default(None)

- The coordinate system to reference when attaching the rib.

### `bDirectByCoord` @type(Boolean) @default(False)

- Whether or not align the rib direction with the coordinate plane defined by the specified coordinate axes.

### `iPlane` @type(Integer) @default(0)

- The coordinate plane:
  - 0: Aligns the rib with the XY plane direction.
  - 1: Aligns the rib with the YZ plane direction.
  - 2: Aligns the rib with the ZX plane direction.

### `dOffsetX` @type(Double) @default(0.0)

- Offset value the rib creation position in X direction.

### `dOffsetY` @type(Double) @default(0.0)

- Offset value the rib creation position in Y direction.

### `dOffsetZ` @type(Double) @default(0.0)

- Offset value the rib creation position in Z direction.

### `bTriangle` @type(Boolean) @default(False)

- Whether creates the rib as a triangular rib with a higher starting point.

### `bPlaneTop` @type(Boolean) @default(True)

- Whether or not makes the rib top flat even when the attachment surface is curved.

### `bCreateNewPart` @type(Boolean) @default(False)

- Whether or not create a rib part as a new part.

### `bMerge` @type(Boolean) @default(True)

- Whether or not merge rib part to the part of target face belongs to.

### `bPreview` @type(Boolean) @default(True)

- Whether or not display preview.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {2-8}
Geometry.Part.Cube()
Assemble.AddRibEx.General(
    dlPositions=[
        [0.007777777777777778, 0.003333333333333333, 0.01], 
        [0.002222222222222222, 0.007777777777777778, 0.01]], 
    crlFaces=[Face(26)], 
    dThickness=0.001, 
    dHeight=0.001)
```
