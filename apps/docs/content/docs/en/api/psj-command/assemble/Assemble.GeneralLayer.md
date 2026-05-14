---
title: "Assemble.GeneralLayer()"
description: "Create a new face inside the part by offsetting a preceding face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > General Layer"
---

## Description

Create a new face inside the part by offsetting a preceding face.

## Syntax

```psj
Assemble.GeneralLayer(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlFaces`

- The list of faces to make layer.
- This is the require input.

<!-- @since:5.0.1 @type:Double @optional @default:1.0 -->
### `dWidth`

- The offset amount for the surface to be created.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iLayer`

- The number of layers to be created.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSeparatePart`

- The enable/disable the option that new layer part will be created in a different body. Boundary layer part and original part have a shared surface.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bForceStitchToSide`

- The enable/disable conform to outside of the model geometry and offset.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bSmoothingEdge`

- The enabledisable prepare the edge of the offset face.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bNoImprint`

- Whether or not imprint the adjacent surface after the creation of the offset face..

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bWidthOnSurface`

- Whether or not interpreted as the amount of offsets along the shape of the model plane.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bMakeHexa`

- Whether or not the make hexa element between layer face and boundary face.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()

creating _status = Assemble.GeneralLayer(crlFaces=[Face(26)])

JPT.Debugger(creating _status)
```
