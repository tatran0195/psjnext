---
title: "Assemble.FullLayer()"
description: "Create a layer (PRISM6 part) with the entire surface mesh of the part offset inward"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Assemble > Full Layer"
---

## Description

Create a layer (PRISM6 part) with the entire surface mesh of the part offset inward.

## Syntax

```psj
Assemble.FullLayer(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crPart

- Specify the target part for create new layers.

<!-- @since:5.0.1 @optional -->
### dLayerWidth

- Specify the layer width.
- The default value is 1.0.

<!-- @since:5.0.1 @optional -->
### iLayer

- Specify number of layer will be created.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### bUsePyramid

- Specify create a pyramid element to tie the layer parts and the internal parts .
- The default value is False.

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
