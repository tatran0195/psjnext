---
title: "BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems()"
description: "Create the centrifugal force load to refer to the coordinate system in the analysis model"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > BodyLoads > CentrifugalForce > CoordinateSystems"
---

## Description

Create the centrifugal force load to refer to the coordinate system in the analysis model.

## Syntax

```psj
BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems(...)
```

## Inputs

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of the target items(Part/Bar) for creating the centrifugal force.

### `strName` @type(String) @default("CentrifugalForce1")

- The name of the centrifugal force load condition to be created.

### `dVelocity` @type(Double) @default(DFLT\_DBL)

- The angular velocity value.

### `dAcceleration` @type(Double) @default(DFLT\_DBL)

- The angular acceleration value.

### `iAxisDirection` @type(Integer) @default(0)

- The rotation axis of coordinate system from X, Y or Z axis.

### `iVelocityUnit` @type(Integer) @default(0)

- The input unit of the angular velocity value.

### `iAccelerationUnit` @type(Integer) @default(0)

- The input unit of the angular acceleration value.

### `crCurCoord` @type(Cursor) @default(None)

- The coordinate system in which the centrifugal force is referenced.

### `crEdit` @type(Cursor) @default(None)

- An existing centrifugal force load. If this parameter is used, the specified centrifugal force load will be modified. If it is lef&#x74;_&#x4E;one_, a new centrifugal force load will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {4,5,6,7,8}
Geometry.Part.Cube()
Tools.Coordinates.ThreeNode(crlNodes=[Node(5, 8, 7)])

created_lbc = BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems(crlTargets=[Part(1)],
                                                                              dVelocity=10.0,
                                                                              dAcceleration=10.0,
                                                                              iAxisDirection=2,
                                                                              crCurCoord=Coord(1))

JPT.Debugger(created_lbc)
```
