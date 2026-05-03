---
title: "Geometry.Transform.Scaling()"
description: "Resize an part about its centroid or a coordinate system. It can resize different dimensions at different scales"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Transform > Scaling"
macro_link: "[ScaleBody](../../macro/geometry/ScaleBody)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Resize an part about its centroid or a coordinate system. It can resize different dimensions at different scales.

## Syntax

```psj
Geometry.Transform.Scaling(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @required

- The parts to be scaled.

### `dlScaleVector` @type(List\[Double]) @default(\[1.0,1.0,1.0])

- The scale vector. It defines how much scaling is done in each direction.

### `dlScaleCenter` @type(List\[Double]) @default(\[0.0,0.0,0.0])

- The scale center. It defines a point about which the given part figure scales.

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate system.

### `bCreateNew` @type(Boolean) @default(False)

- Whether to create new part or attach to original parts.

### `bCopyLbc` @type(Boolean) @default(False)

- Whether to copy load boundary condition of original part to scaled part.

### `bCopyProperty` @type(Boolean) @default(False)

- Whether to copy property of original part to scaled part.

### `bUsePartCenter` @type(Boolean) @default(True)

- Whether to use original part center as scaled center.

### `bCopyReference` @type(Boolean) @default(False) @since(5.1.0)

- Whether to copy references from the existing part to the created parts or not.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7}
Geometry.Part.Cube()

scaling_status = Geometry.Transform.Scaling(crlParts=[Part(1)], 
                                            dlScaleVector=[1.5, 
                                                           0.5, 
                                                           0.5], 
                                            bCreateNew=True)

JPT.Debugger(scaling_status)
```
