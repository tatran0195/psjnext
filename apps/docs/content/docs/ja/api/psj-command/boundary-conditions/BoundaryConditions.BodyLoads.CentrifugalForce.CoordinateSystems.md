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

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of the target items(Part/Bar) for creating the centrifugal force.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the centrifugal force load condition to be created.
- The default value is "CentrifugalForce1".

<!-- @since:5.0.1 @optional -->
### dVelocity

- Specify the angular velocity value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dAcceleration

- Specify the angular acceleration value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iAxisDirection

- Specify the rotation axis of coordinate system from X, Y or Z axis.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iVelocityUnit

- Specify the input unit of the angular velocity value.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAccelerationUnit

- Specify the input unit of the angular acceleration value.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCurCoord

- Specify the coordinate system in which the centrifugal force is referenced.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing centrifugal force load. If this parameter is used, the specified centrifugal force load will be modified. If it is left _None_, a new centrifugal force load will be created.
- The default value is _None_.

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
