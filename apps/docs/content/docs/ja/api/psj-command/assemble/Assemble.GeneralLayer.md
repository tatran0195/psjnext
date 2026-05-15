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

<!-- @since:5.0.1 @optional -->
### crlFaces

- Specify the list of faces to make layer.
- This is the require input.

<!-- @since:5.0.1 @optional -->
### dWidth

- Specify the offset amount for the surface to be created.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iLayer

- Specify the number of layers to be created.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bSeparatePart

- Specify new layer part will be created in a different body. Boundary layer part and original part have a shared surface.
- The default value is False.

### `bForceStitchToSide`

- A _Boolean_ enable/disable conform to outside of the model geometry and offset.
- The default value is False.

### `bSmoothingEdge`

- A _Boolean_ enabledisable prepare the edge of the offset face.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bNoImprint

- Specify whether or not imprint the adjacent surface after the creation of the offset face..
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bWidthOnSurface

- Specify whether or not interpreted as the amount of offsets along the shape of the model plane.
- The default value is False.

<!-- @since:5.0.1 @optional -->
### bMakeHexa

- Specify whether or not the make hexa element between layer face and boundary face.
- The default value is False.

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
