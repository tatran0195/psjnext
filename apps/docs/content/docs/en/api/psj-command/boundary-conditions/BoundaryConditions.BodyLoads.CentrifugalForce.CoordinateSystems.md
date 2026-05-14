---
title: "BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems()"
description: "Create the centrifugal force load to refer to the coordinate system in the analysis model"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "BoundaryConditions > BodyLoads > CentrifugalForce > CoordinateSystems"
---

## Description

Create the centrifugal force load to refer to the coordinate system in the analysis model.

## Syntax

```psj
BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems(...)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of the target items(Part/Bar) for creating the centrifugal force.

<!-- @since:5.0.1 @type:String @optional @default:"CentrifugalForce1" -->
### `strName`

- The name of the centrifugal force load condition to be created.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dVelocity`

- The angular velocity value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dAcceleration`

- The angular acceleration value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAxisDirection`

- The rotation axis of coordinate system from X, Y or Z axis.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iVelocityUnit`

- The input unit of the angular velocity value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iAccelerationUnit`

- The input unit of the angular acceleration value.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCurCoord`

- The coordinate system in which the centrifugal force is referenced.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing centrifugal force load. If this parameter is used, the specified centrifugal force load will be modified. If it is left _None_, a new centrifugal force load will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {4,5,6,7,8}
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(5, 8, 7)])

created _lbc = BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems(crlTargets=[Part(1)],
                                                                              dVelocity=10.0,
                                                                              dAcceleration=10.0,
                                                                              iAxisDirection=2,
                                                                              crCurCoord=Coord(1))

JPT.Debugger(created _lbc)
```
