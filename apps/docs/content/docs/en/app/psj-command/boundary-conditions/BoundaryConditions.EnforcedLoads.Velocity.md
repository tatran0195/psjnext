---
title: "BoundaryConditions.EnforcedLoads.Velocity()"
description: "Create enforced velocity to face, edge or node. User inputs enforced velocity parameters, and it will return enforced velocity to the specified location"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > Enforced Loads > Velocity"
---

## Description

Create enforced velocity to face, edge or node. User inputs enforced velocity parameters, and it will return enforced velocity to the specified location.

## Syntax

```psj
BoundaryConditions.EnforcedLoads.Velocity(...)
```

## Inputs

### `strName` @type(String) @default("EnforcedVelocity1")

- The enforced velocity load name.

### `enforceVelocity` @type(ENFORCED\_VELOCITY\_LBC) @required

- The enforced velocity parameters.

### `crlTargets` @type(List\[Cursor]) @required

- The list of targets to apply enforced velocity. Target can be face, edge or node.

### `crEdit` @type(Cursor) @default(None)

- An existing enforced velocity.
  - If this parameter is used, the specified enforced velocity will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new enforced velocity will be created.

### `bADVCStatic` @type(Boolean) @default(False)

- Whether to create 2 ADVC Static processes for bolt fix length or not.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5}
Geometry.Part.Cube()

created_bcs = BoundaryConditions.EnforcedLoads.Velocity(enforceVelocity=ENFORCED_VELOCITY_LBC(iDwDof=1,
                                                                                              dVelocityTX=0.001), 
                                                        crlTargets=[Face(24)])

JPT.Debugger(created_bcs)
```
