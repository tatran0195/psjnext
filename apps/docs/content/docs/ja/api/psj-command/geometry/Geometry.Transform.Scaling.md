---
title: "Geometry.Transform.Scaling()"
description: "Resize an part about its centroid or a coordinate system. It can resize different dimensions at different scales"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Transform > Scaling"
macro _link: "[ScaleBody](../../macro/geometry/ScaleBody)"
---

## Description

Resize an part about its centroid or a coordinate system. It can resize different dimensions at different scales.

## Syntax

```psj
Geometry.Transform.Scaling(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### crlParts

- Specify the parts to be scaled.

<!-- @since:5.0.1 @optional -->
### dlScaleVector

- Specify the scale vector. It defines how much scaling is done in each direction.
- The default value is \[1.0,1.0,1.0].

<!-- @since:5.0.1 @optional -->
### dlScaleCenter

- Specify the scale center. It defines a point about which the given part figure scales.
- The default value is \[0.0,0.0,0.0].

<!-- @since:5.0.1 @optional -->
### crCoordinate

- Specify the coordinate system.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### bCreateNew

- Specify whether to create new part or attach to original parts.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyLbc

- Specify whether to copy load boundary condition of original part to scaled part.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bCopyProperty

- Specify whether to copy property of original part to scaled part.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### bUsePartCenter

- Specify whether to use original part center as scaled center.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bCopyReference

- Specify whether to copy references from the existing part to the created parts or not.
- The default value is _False_.

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7}
Geometry.Part.Cube()

scaling _status = Geometry.Transform.Scaling(crlParts=[Part(1)], 
                                            dlScaleVector=[1.5, 
                                                           0.5, 
                                                           0.5], 
                                            bCreateNew=True)

JPT.Debugger(scaling _status)
```
