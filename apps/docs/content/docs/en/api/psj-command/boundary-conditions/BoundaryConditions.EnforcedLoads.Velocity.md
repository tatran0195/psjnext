---
title: "BoundaryConditions.EnforcedLoads.Velocity()"
description: "Create enforced velocity to face, edge or node. User inputs enforced velocity parameters, and it will return enforced velocity to the specified location"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > Enforced Loads > Velocity"
---

## Description

Create enforced velocity to face, edge or node. User inputs enforced velocity parameters, and it will return enforced velocity to the specified location.

## Syntax

```psj
BoundaryConditions.EnforcedLoads.Velocity(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"EnforcedVelocity1" -->
### `strName`

- The enforced velocity load name.

<!-- @since:5.0.1 @type:ENFORCED _VELOCITY _LBC @required -->
### `enforceVelocity`

- The enforced velocity parameters.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The list of targets to apply enforced velocity. Target can be face, edge or node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing enforced velocity.
  - If this parameter is used, the specified enforced velocity will be modified.
  - If it is left _None_, a new enforced velocity will be created.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `bADVCStatic`

- Whether to create 2 ADVC Static processes for bolt fix length or not.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.EnforcedLoads.Velocity(enforceVelocity=ENFORCED _VELOCITY _LBC(iDwDof=1,
                                                                                              dVelocityTX=0.001), 
                                                        crlTargets=[Face(24)])

JPT.Debugger(created _bcs)
```
