---
title: "BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions()"
description: "Create the centrifugal force load in the analysis model"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > BodyLoads > CentrifugalForce > TwoPositions"
---

## Description

Create the centrifugal force load in the analysis model.

## Syntax

```psj
BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of the target items for creating the centrifugal force.

<!-- @since:5.0.1 @type:String @optional @default:"CentrifugalForce1" -->
### `strName`

- The name of the centrifugal force load condition to be created.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dBasePointX`

- The X coordinate of the rotation axis reference point.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dBasePointY`

- The Y coordinate of the rotation axis reference point.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dBasePointZ`

- The Z coordinate of the rotation axis reference point.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTipPointX`

- The X coordinate of the rotation axis vertex.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTipPointY`

- The Y coordinate of the rotation axis vertex.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTipPointZ`

- The Z coordinate of the rotation axis vertex.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dVelocity`

- The angular velocity value.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dAcceleration`

- The angular acceleration value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iVelocityUnit`

- The input unit of the angular velocity value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAccelerationUnit`

- The input unit of the angular acceleration value.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing centrifugal force load. If this parameter is used, the specified centrifugal force load will be modified. If it is left _None_, a new centrifugal force load will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created _lbc = BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions(crlTargets=[Part(1),
                                                                                     Node(5, 3)],
                                                                         dBasePointZ=0.01,
                                                                         dTipPointX=0.01,
                                                                         dTipPointY=0.01,
                                                                         dVelocity=10.0,
                                                                         dAcceleration=10.0)

JPT.Debugger(created _lbc)
```
