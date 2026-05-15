---
title: "Assemble.AddRibEx.FromEdge()"
description: "Specify an edge to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Assemble > AddRibEx > FromEdge"
macro _link: "AddRibFromEdgesEx"
---

## Description

Specify an edge to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh.

## Syntax

```psj
Assemble.AddRibEx.FromEdge(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### crlFaces

- Specify the target face where the created rib will be attached.

<!-- @since:5.1.0 @required -->
### crlEdges

- Specify edge where the rib created from.

<!-- @since:5.1.0 @optional -->
### dThickness

- Specify the width of the rib.
- The default value is 0.001.

<!-- @since:5.1.0 @optional -->
### dHeight

- Specify the height of the rib from the attachment surface.
- The default value is 0.001.

<!-- @since:5.1.0 @optional -->
### iDirection

- Specify the direction of the rib from the attachment surface.
  - 0: Normal Offset
  - 1: Offset
  - 2: Projection
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify the coordinate system to reference when attaching the rib.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### iBasePlane

- Specify the direction of rib extrusion when Offset or Projection is selected for Direction.
  - 0: XY plane
  - 1: YZ plane
  - 2: XZ plane
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dOffsetX

- Specify the offset value the rib creation position in X direction.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dOffsetY

- Specify the offset value the rib creation position in Y direction.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dOffsetZ

- Specify the offset value the rib creation position in Z direction.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iRibTriangle

- Specify to make the rib triangular.
  - 0: Creates a normal rib without making it triangular.
  - 1: Creates a triangular rib with a higher starting point.
  - 2: Creates a triangular rib with a higher ending point.

<!-- @since:5.1.0 @optional -->
### bCreateNewPart

- Specify whether or not to create the rib as a new part.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bMerge

- Specify whether or not to merge the rib with the attachment part.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bPreview

- Specify whether or not to display preview.
- The default value is _True_.

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
