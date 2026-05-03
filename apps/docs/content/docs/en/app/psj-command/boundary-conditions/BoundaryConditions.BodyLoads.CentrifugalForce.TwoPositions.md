---
title: "BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions()"
description: "Create the centrifugal force load in the analysis model"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > BodyLoads > CentrifugalForce > TwoPositions"
---

## Description

Create the centrifugal force load in the analysis model.

## Syntax

```psj
BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of the target items for creating the centrifugal force.

### `strName` @type(String) @default("CentrifugalForce1")

- The name of the centrifugal force load condition to be created.

### `dBasePointX` @type(Double) @default(0.0)

- The X coordinate of the rotation axis reference point.

### `dBasePointY` @type(Double) @default(0.0)

- The Y coordinate of the rotation axis reference point.

### `dBasePointZ` @type(Double) @default(0.0)

- The Z coordinate of the rotation axis reference point.

### `dTipPointX` @type(Double) @default(0.0)

- The X coordinate of the rotation axis vertex.

### `dTipPointY` @type(Double) @default(0.0)

- The Y coordinate of the rotation axis vertex.

### `dTipPointZ` @type(Double) @default(0.0)

- The Z coordinate of the rotation axis vertex.

### `dVelocity` @type(Double) @default(0.0)

- The angular velocity value.

### `dAcceleration` @type(Double) @default(0.0)

- The angular acceleration value.

### `iVelocityUnit` @type(Integer) @default(0)

- The input unit of the angular velocity value.

### `iAccelerationUnit` @type(Integer) @default(0)

- The input unit of the angular acceleration value.

### `crEdit` @type(Cursor) @default(None)

- An existing centrifugal force load. If this parameter is used, the specified centrifugal force load will be modified. If it is lef&#x74;_&#x4E;one_, a new centrifugal force load will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6,7,8,9}
Geometry.Part.Cube()

created_lbc = BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions(crlTargets=[Part(1),
                                                                                     Node(5, 3)],
                                                                         dBasePointZ=0.01,
                                                                         dTipPointX=0.01,
                                                                         dTipPointY=0.01,
                                                                         dVelocity=10.0,
                                                                         dAcceleration=10.0)

JPT.Debugger(created_lbc)
```
