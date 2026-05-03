---
title: "Connections.RigidWall()"
description: "Define a rigid wall contact setting to simulate impact analyses with planar rigid walls"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidWall"
---

## Description

Define a rigid wall contact setting to simulate impact analyses with planar rigid walls.

## Syntax

```psj
Connections.RigidWall(...)
```

## Inputs

### `strName` @type(String) @default("RigidWall1")

- The rigid wall name.

### `iObject` @type(Integer) @default(0)

- The rigid object type.
  - 0: Planar rigid object.

### `iType` @type(Integer) @default(0)

- The rigid wall type.
  - 0: Infinite body.
  - 1: Finite body.

### `iMotion` @type(Integer) @default(0)

- The behavior.
  - 0: Static - Stationary.
  - 1: Moving - Movable.

### `iFriction` @type(Integer) @default(0)

- The condition of friction types. The friction type of rigid wall contact definition is one of the following.
  - 0: Frictionless - No friction.
  - 1: No Sliding - No slip.
  - 2: Coulomb Friction - Coulomb friction.
  - 3: Weld with Frictionless - Frictionless welding.
  - 4: Weld with No Sliding - Non-slip welding.

### `iOrthoFriction` @type(Integer) @default(0)

- Whether or not using rigid orthotropic frictional coefficient.
  - 0: No
  - 1: Yes

### `iForces` @type(Integer) @default(0)

- Whether or not considering the reaction force.
  - 0: No
  - 1: Yes

### `dFinite1` @type(Double) @default(DFLT\_DBL)

- Length of l(x) edge when Finite body is used.

### `dFinite2` @type(Double) @default(DFLT\_DBL)

- Length of m(y) edge when Finite body is used.

### `dMotionMass` @type(Double) @default(DFLT\_DBL)

- The motion mass when Moving behavior is used.

### `dMotionInitVelocity` @type(Double) @default(DFLT\_DBL)

- The motion initial velocity Moving behavior is used.

### `dFricCoulombCoeff` @type(Double) @default(DFLT\_DBL)

- The friction coulomb coefficient when Coulomb Friction is used.

### `dFricWeldVelocity` @type(Double) @default(DFLT\_DBL)

- The critical normal velocity for weld when Frictionless welding is used.

### `iForcesCirclesNum` @type(Integer) @default(0)

- The number of forces cycles when reaction force is used.

### `dOrthoStaticCoeff1` @type(Double) @default(DFLT\_DBL)

- The ortho static friction coefficient a when rigid Ortho is used.

### `dOrthoStaticCoeff2` @type(Double) @default(DFLT\_DBL)

- The ortho static friction coefficient b when rigid Ortho is used.

### `dOrthoDynamicCoeff1` @type(Double) @default(DFLT\_DBL)

- The ortho dynamic friction coefficient a when rigid Ortho is used.

### `dOrthoDynamicCoeff2` @type(Double) @default(DFLT\_DBL)

- The ortho dynamic friction coefficient b when rigid Ortho is used.

### `dOrthoDecayConst1` @type(Double) @default(DFLT\_DBL)

- The decay constant a-direction a.

### `dOrthoDecayConst2` @type(Double) @default(DFLT\_DBL)

- The decay constant a-direction b.

### `dOrthoFricVector1` @type(Double) @default(DFLT\_DBL)

- The ortho Friction Vector - x value.

### `dOrthoFricVector2` @type(Double) @default(DFLT\_DBL)

- The ortho Friction Vector - y value.

### `dOrthoFricVector3` @type(Double) @default(DFLT\_DBL)

- The ortho Friction Vector - z value.

### `bAllNodeSlave` @type(Boolean) @default(False)

- Whether or not considering all nodes to be subordinate points.

### `crCoord` @type(Cursor) @default(None)

- The local coordinate. If th&#x65;_&#x63;rCoor&#x64;_&#x64;oes not specify any local coordinate, function will execute with global coordinate.

### `crAreaFaceSet` @type(Cursor) @default(None)

- The Selected Force Area Face when reaction force is used.

### `crVisualNodeSet` @type(Cursor) @default(None)

- The Selected Visualization Node Set when reaction force is used.

### `crlTargets` @type(List\[Cursor])

- The list of targets will be set up as rigid wall.
- This is the required input.

### `crEdit` @type(Cursor) @default(None)

- An existing rigid wall contact setting. If this parameter is used, the specified rigid wall contact setting will be modified. When the default value is used, a new rigid wall contact setting will be created.

## Return Code

A _Cursor_ specifying the created or the modified rigid wall contact connection.

## Sample Code

```psj {2}
Geometry.Part.Cube(iPartColor=16053365)
created_wall = Connections.RigidWall(crlTargets=[Face(24)])
JPT.Debugger(created_wall)
```
