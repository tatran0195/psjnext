---
title: "Assemble.AddRibEx.General()"
description: "Add rib part on a part."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Assemble > AddRibEx > General"
macro _link: "AddRibGeneralEx"
---

## Description

Add rib part on a part.

## Syntax

```psj
Assemble.AddRibEx.General(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Double] @required -->
### `dlPositions`

- The position of first end of the rib to create.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlFaces`

- The position of second end of the rib to create.

<!-- @since:5.1.0 @type:Double @optional @default:0.0005 -->
### `dThickness`

- The width of the rib.

<!-- @since:5.1.0 @type:Double @optional @default:0.001 -->
### `#dHeight`

- The height of the rib from the attachment surface.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `#crCoordinate`

- The coordinate system to reference when attaching the rib.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDirectByCoord`

- Whether or not align the rib direction with the coordinate plane defined by the specified coordinate axes.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iPlane`

- The coordinate plane:
  - 0: Aligns the rib with the XY plane direction.
  - 1: Aligns the rib with the YZ plane direction.
  - 2: Aligns the rib with the ZX plane direction.

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
### `bTriangle`

- Whether creates the rib as a triangular rib with a higher starting point.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bPlaneTop`

- Whether or not makes the rib top flat even when the attachment surface is curved.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCreateNewPart`

- Whether or not create a rib part as a new part.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMerge`

- Whether or not merge rib part to the part of target face belongs to.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bPreview`

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
