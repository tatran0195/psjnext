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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the enforced velocity load name.
- The default value is "EnforcedVelocity1".

<!-- @since:5.0.1 @required -->
### enforceVelocity

- Specify the enforced velocity parameters.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the list of targets to apply enforced velocity. Target can be face, edge or node.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing enforced velocity.
  - If this parameter is used, the specified enforced velocity will be modified.
  - If it is left _None_, a new enforced velocity will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### bADVCStatic

- Specify whether to create 2 ADVC Static processes for bolt fix length or not.
- The default value is _False_.

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
