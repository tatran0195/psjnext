---
title: "Assemble.AddRibEx.Curve()"
description: "Specify multiple points to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Assemble > AddRibEx > Curve"
macro_link: "AddRibCurveEx"
---

## Description

Specify multiple points to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh.

## Syntax

```psj
Assemble.AddRibEx.Curve(...)
```

## Inputs

### `dlPositions` @type(List\[Double]) @required

- Positions of control points of curved rib.

### `crlFaces` @type(List\[Cursor]) @required

- The target face where the created rib will be attached.

### `dThickness` @type(Double) @default(0.001)

- The width of the rib.

### `dHeight` @type(Double) @default(0.001)

- The height of the rib from the attachment surface.

### `iDirection` @type(Int) @default(0)

- The direction of the rib from the attachment surface.
  - 0: Normal Offset
  - 1: Offset
  - 2: Projection

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate system to reference when attaching the rib.

### `iBasePlane` @type(Integer) @default(0)

- The direction of rib extrusion when Offset or Projection is selected for Direction.
  - 0: XY plane
  - 1: YZ plane
  - 2: XZ plane

### `dOffsetX` @type(Double) @default(0.0)

- The offset value the rib creation position in X direction.

### `dOffsetY` @type(Double) @default(0.0)

- The offset value the rib creation position in Y direction.

### `dOffsetZ` @type(Double) @default(0.0)

- The offset value the rib creation position in Z direction.

### `bSpline` @type(Boolean) @default(False)

- Whether or not calculate a spline curve from the input points to define the rib path.

### `iTriangleType` @type(Integer) @default(0)

- To make the rib triangular.
  - 0: Creates a normal rib without making it triangular.
  - 1: Creates a triangular rib with a higher starting point.
  - 2: Creates a triangular rib with a higher ending point.

### `bCreateNewPart` @type(Boolean) @default(False)

- Whether or not to create the rib as a new part.

### `bMerge` @type(Boolean) @default(True)

- Whether or not to merge the rib with the attachment part.

### `bPreview` @type(Boolean) @default(True)

- Whether or not to display preview.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {3-12}
Geometry.Part.Cube()

Assemble.AddRibEx.Curve(
  dOffsetX=2.22222e-06, 
  dOffsetY=1.11111e-06, 
  dOffsetZ=1e-05, 
  dlPositions=[
    [0.002222222222222222, 0.001111111111111111, 0.01], 
    [0.005555555555555556, 0.003333333333333333, 0.01], 
    [0.006666666666666666, 0.006666666666666666, 0.01], 
    [0.003333333333333333, 0.008888888888888889, 0.01]], 
    crlFaces=[Face(26)])
```
