---
title: "Assemble.FullLayer()"
description: "Create a layer (PRISM6 part) with the entire surface mesh of the part offset inward"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Assemble > Full Layer"
---

## Description

Create a layer (PRISM6 part) with the entire surface mesh of the part offset inward.

## Syntax

```psj
Assemble.FullLayer(...)
```

## Inputs

### `crPart` @type(Cursor) @required

- The target part for create new layers.

### `dLayerWidth` @type(Double) @default(1.0)

- The layer width.

### `iLayer` @type(Integer) @default(1)

- Number of layer will be created.

### `bUsePyramid` @type(Boolean) @default(False)

- Enable/disable option that create a pyramid element to tie the layer parts and the internal parts .

## Return Code

A _Boolean_ specifying whether the function is executed correctly or not:

- _True_: The function is executed without any problems.
- _False_: The function cannot be executed.

## Sample Code

```psj {2}
cube = Geometry.Part.Cube()
flag = Assemble.FullLayer(crPart=cube)
JPT.Debugger(flag)
```
