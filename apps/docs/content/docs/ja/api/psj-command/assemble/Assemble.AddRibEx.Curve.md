---
title: "Assemble.AddRibEx.Curve()"
description: "Specify multiple points to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Assemble > AddRibEx > Curve"
macro _link: "AddRibCurveEx"
---

## Description

Specify multiple points to define the path of the rib and the attachment surface, and add the rib shape to the existing surface mesh.

## Syntax

```psj
Assemble.AddRibEx.Curve(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### dlPositions

- Specify positions of control points of curved rib.

<!-- @since:5.1.0 @required -->
### crlFaces

- Specify the target face where the created rib will be attached.

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
### bSpline

- Specify whether or not calculate a spline curve from the input points to define the rib path.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iTriangleType

- Specify to make the rib triangular.
  - 0: Creates a normal rib without making it triangular.
  - 1: Creates a triangular rib with a higher starting point.
  - 2: Creates a triangular rib with a higher ending point.
- The default value is 0.

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
