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

<!-- @since:5.1.0 @type:List[Double] @required -->
### `dlPositions`

- The positions of control points of curved rib.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlFaces`

- The target face where the created rib will be attached.

<!-- @since:5.1.0 @type:Double @optional @default:0.001 -->
### `dThickness`

- The width of the rib.

<!-- @since:5.1.0 @type:Double @optional @default:0.001 -->
### `dHeight`

- The height of the rib from the attachment surface.

<!-- @since:5.1.0 @type:Int @optional @default:0 -->
### `iDirection`

- The direction of the rib from the attachment surface.
  - 0: Normal Offset
  - 1: Offset
  - 2: Projection

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The coordinate system to reference when attaching the rib.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBasePlane`

- The direction of rib extrusion when Offset or Projection is selected for Direction.
  - 0: XY plane
  - 1: YZ plane
  - 2: XZ plane

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dOffsetX`

- The offset value the rib creation position in X direction.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dOffsetY`

- The offset value the rib creation position in Y direction.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dOffsetZ`

- The offset value the rib creation position in Z direction.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bSpline`

- Whether or not calculate a spline curve from the input points to define the rib path.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTriangleType`

- The to make the rib triangular.
  - 0: Creates a normal rib without making it triangular.
  - 1: Creates a triangular rib with a higher starting point.
  - 2: Creates a triangular rib with a higher ending point.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCreateNewPart`

- Whether or not to create the rib as a new part.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMerge`

- Whether or not to merge the rib with the attachment part.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bPreview`

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
