---
title: "Assemble.GeneralLayer()"
description: "Create a new face inside the part by offsetting a preceding face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assemble > General Layer"
---

## Description

Create a new face inside the part by offsetting a preceding face.

## Syntax

```psj
Assemble.GeneralLayer(...)
```

## Inputs

### `crlFaces` @type(List\[Cursor])

- The list of faces to make layer.
- This is the require input.

### `dWidth` @type(Double) @default(1.0)

- The offset amount for the surface to be created.

### `iLayer` @type(Integer) @default(1)

- The number of layers to be created.

### `bSeparatePart` @type(Boolean) @default(False)

- Enable/disable the option that new layer part will be created in a different body. Boundary layer part and original part have a shared surface.

### `bForceStitchToSide` @type(Boolean) @default(False)

- Enable/disable conform to outside of the model geometry and offset.

### `bSmoothingEdge` @type(Boolean) @default(False)

- Enabledisable prepare the edge of the offset face.

### `bNoImprint` @type(Boolean) @default(False)

- Whether or not imprint the adjacent surface after the creation of the offset face..

### `bWidthOnSurface` @type(Boolean) @default(False)

- Whether or not interpreted as the amount of offsets along the shape of the model plane.

### `bMakeHexa` @type(Boolean) @default(False)

- Whether or not the make hexa element between layer face and boundary face.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3}
Geometry.Part.Cube()

creating_status = Assemble.GeneralLayer(crlFaces=[Face(26)])

JPT.Debugger(creating_status)
```
