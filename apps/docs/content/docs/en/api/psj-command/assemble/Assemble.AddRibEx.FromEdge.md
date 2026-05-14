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

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlFaces`

- The target face where the created rib will be attached.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlEdges`

- The edge where the rib created from.

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

<!-- @since:5.1.0 @type:Integer @optional -->
### `iRibTriangle`

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
