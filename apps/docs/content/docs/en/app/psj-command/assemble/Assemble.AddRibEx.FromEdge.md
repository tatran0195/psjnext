---
title: "Assemble.AddRibEx.FromEdge()"
description: "Specify an edge to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Assemble > AddRibEx > FromEdge"
macro_link: "AddRibFromEdgesEx"
---

## Description

Specify an edge to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh.

## Syntax

```psj
Assemble.AddRibEx.FromEdge(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor]) @required

- The target face where the created rib will be attached.

### `crlEdges` @type(List\[Cursor]) @required

- Edge where the rib created from.

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

### `iRibTriangle` @type(Integer)

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

A _Boolean_ specifying

## Sample Code

```psj {11-15}
Geometry.Part.Cube(iPartColor=11776856)

Geometry.Edge.Spline(
    dllPoints=[
        [0.003333333333333333, 0.001111111111111111, 0.01], 
        [0.002222222222222222, 0.007777777777777778, 0.01], 
        [0.006666666666666666, 0.005555555555555556, 0.01], 
        [0.008888888888888889, 0.006666666666666666, 0.01]], 
    crlFaces=[Face(26)])

Assemble.AddRibEx.FromEdge(
    crlFaces=[Face(26)], 
    crlEdges=[Edge(41)], 
    dThickness=0.001, 
    dHeight=0.001)
```
