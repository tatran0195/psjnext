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

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of the target items for creating the centrifugal force.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the centrifugal force load condition to be created.
- The default value is "CentrifugalForce1".

<!-- @since:5.0.1 @optional -->
### dBasePointX

- Specify the X coordinate of the rotation axis reference point.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dBasePointY

- Specify the Y coordinate of the rotation axis reference point.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dBasePointZ

- Specify the Z coordinate of the rotation axis reference point.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dTipPointX

- Specify the X coordinate of the rotation axis vertex.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dTipPointY

- Specify the Y coordinate of the rotation axis vertex.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dTipPointZ

- Specify the Z coordinate of the rotation axis vertex.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dVelocity

- Specify the angular velocity value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dAcceleration

- Specify the angular acceleration value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iVelocityUnit

- Specify the input unit of the angular velocity value.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iAccelerationUnit

- Specify the input unit of the angular acceleration value.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing centrifugal force load. If this parameter is used, the specified centrifugal force load will be modified. If it is left _None_, a new centrifugal force load will be created.
- The default value is _None_.

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
