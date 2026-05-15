---
title: "Connections.RigidWall()"
description: "Define a rigid wall contact setting to simulate impact analyses with planar rigid walls"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidWall"
---

## Description

Define a rigid wall contact setting to simulate impact analyses with planar rigid walls.

## Syntax

```psj
Connections.RigidWall(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the rigid wall name.
- The default value is "RigidWall1".

<!-- @since:5.0.1 @optional -->
### iObject

- Specify the rigid object type.
  - 0: Planar rigid object.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iType

- Specify the rigid wall type.
  - 0: Infinite body.
  - 1: Finite body.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMotion

- Specify the behavior.
  - 0: Static - Stationary.
  - 1: Moving - Movable.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iFriction

- Specify the condition of friction types. The friction type of rigid wall contact definition is one of the following.
  - 0: Frictionless - No friction.
  - 1: No Sliding - No slip.
  - 2: Coulomb Friction - Coulomb friction.
  - 3: Weld with Frictionless - Frictionless welding.
  - 4: Weld with No Sliding - Non-slip welding.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iOrthoFriction

- Specify whether or not using rigid orthotropic frictional coefficient.
  - 0: No
  - 1: Yes
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iForces

- Specify whether or not considering the reaction force.
  - 0: No
  - 1: Yes
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dFinite1

- Specify length of l(x) edge when Finite body is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dFinite2

- Specify length of m(y) edge when Finite body is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMotionMass

- Specify the motion mass when Moving behavior is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dMotionInitVelocity

- Specify the motion initial velocity Moving behavior is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dFricCoulombCoeff

- Specify the friction coulomb coefficient when Coulomb Friction is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dFricWeldVelocity

- Specify the critical normal velocity for weld when Frictionless welding is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### iForcesCirclesNum

- Specify the number of forces cycles when reaction force is used.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dOrthoStaticCoeff1

- Specify the ortho static friction coefficient a when rigid Ortho is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dOrthoStaticCoeff2

- Specify the ortho static friction coefficient b when rigid Ortho is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dOrthoDynamicCoeff1

- Specify the ortho dynamic friction coefficient a when rigid Ortho is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dOrthoDynamicCoeff2

- Specify the ortho dynamic friction coefficient b when rigid Ortho is used.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dOrthoDecayConst1

- Specify the decay constant a-direction a.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dOrthoDecayConst2

- Specify the decay constant a-direction b.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dOrthoFricVector1

- Specify the ortho Friction Vector - x value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dOrthoFricVector2

- Specify the ortho Friction Vector - y value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### dOrthoFricVector3

- Specify the ortho Friction Vector - z value.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### bAllNodeSlave

- Specify whether or not considering all nodes to be subordinate points.
- The default value is _False_.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the local coordinate. If the _crCoord_ does not specify any local coordinate, function will execute with global coordinate.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crAreaFaceSet

- Specify the Selected Force Area Face when reaction force is used.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crVisualNodeSet

- Specify the Selected Visualization Node Set when reaction force is used.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of targets will be set up as rigid wall.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing rigid wall contact setting. If this parameter is used, the specified rigid wall contact setting will be modified. When the default value is used, a new rigid wall contact setting will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created or the modified rigid wall contact connection.

## Sample Code

```psj {2}
Geometry.Part.Cube(iPartColor=16053365)
created _wall = Connections.RigidWall(crlTargets=[Face(24)])
JPT.Debugger(created _wall)
```
