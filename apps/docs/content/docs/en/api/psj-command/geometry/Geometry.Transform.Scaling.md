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

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlParts`

- The parts to be scaled.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[1.0,1.0,1.0] -->
### `dlScaleVector`

- The scale vector. It defines how much scaling is done in each direction.

<!-- @since:5.0.1 @type:List[Double] @optional @default:[0.0,0.0,0.0] -->
### `dlScaleCenter`

- The scale center. It defines a point about which the given part figure scales.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The coordinate system.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCreateNew`

- Whether to create new part or attach to original parts.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyLbc`

- Whether to copy load boundary condition of original part to scaled part.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bCopyProperty`

- Whether to copy property of original part to scaled part.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUsePartCenter`

- Whether to use original part center as scaled center.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCopyReference`

- Whether to copy references from the existing part to the created parts or not.

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
