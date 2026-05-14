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

<!-- @since:5.0.1 @type:String @optional @default:"RigidWall1" -->
### `strName`

- The rigid wall name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iObject`

- The rigid object type.
  - 0: Planar rigid object.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The rigid wall type.
  - 0: Infinite body.
  - 1: Finite body.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMotion`

- The behavior.
  - 0: Static - Stationary.
  - 1: Moving - Movable.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iFriction`

- The condition of friction types. The friction type of rigid wall contact definition is one of the following.
  - 0: Frictionless - No friction.
  - 1: No Sliding - No slip.
  - 2: Coulomb Friction - Coulomb friction.
  - 3: Weld with Frictionless - Frictionless welding.
  - 4: Weld with No Sliding - Non-slip welding.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iOrthoFriction`

- Whether or not using rigid orthotropic frictional coefficient.
  - 0: No
  - 1: Yes

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iForces`

- Whether or not considering the reaction force.
  - 0: No
  - 1: Yes

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFinite1`

- The length of l(x) edge when Finite body is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFinite2`

- The length of m(y) edge when Finite body is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMotionMass`

- The motion mass when Moving behavior is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dMotionInitVelocity`

- The motion initial velocity Moving behavior is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFricCoulombCoeff`

- The friction coulomb coefficient when Coulomb Friction is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dFricWeldVelocity`

- The critical normal velocity for weld when Frictionless welding is used.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iForcesCirclesNum`

- The number of forces cycles when reaction force is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoStaticCoeff1`

- The ortho static friction coefficient a when rigid Ortho is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoStaticCoeff2`

- The ortho static friction coefficient b when rigid Ortho is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoDynamicCoeff1`

- The ortho dynamic friction coefficient a when rigid Ortho is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoDynamicCoeff2`

- The ortho dynamic friction coefficient b when rigid Ortho is used.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoDecayConst1`

- The decay constant a-direction a.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoDecayConst2`

- The decay constant a-direction b.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoFricVector1`

- The ortho Friction Vector - x value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoFricVector2`

- The ortho Friction Vector - y value.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dOrthoFricVector3`

- The ortho Friction Vector - z value.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bAllNodeSlave`

- Whether or not considering all nodes to be subordinate points.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The local coordinate. If the _crCoord_ does not specify any local coordinate, function will execute with global coordinate.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crAreaFaceSet`

- The Selected Force Area Face when reaction force is used.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crVisualNodeSet`

- The Selected Visualization Node Set when reaction force is used.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlTargets`

- The list of targets will be set up as rigid wall.
- This is the required input.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing rigid wall contact setting. If this parameter is used, the specified rigid wall contact setting will be modified. When the default value is used, a new rigid wall contact setting will be created.

## Return Code

A _Cursor_ specifying the created or the modified rigid wall contact connection.

## Sample Code

```psj {2}
Geometry.Part.Cube(iPartColor=16053365)
created _wall = Connections.RigidWall(crlTargets=[Face(24)])
JPT.Debugger(created _wall)
```
