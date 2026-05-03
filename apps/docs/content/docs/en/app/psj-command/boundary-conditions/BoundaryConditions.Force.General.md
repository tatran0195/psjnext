---
title: "BoundaryConditions.Force.General()"
description: "Create a general force applied to the selected Face, Edge or Node. User inputs the force values and it will apply the force to the selected items"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > Force > General"
---

## Description

Create a general force applied to the selected Face, Edge or Node. User inputs the force values and it will apply the force to the selected items.

## Syntax

```psj
BoundaryConditions.Force.General(...)
```

## Inputs

### `strName` @type(String) @default("Force1")

- The name of force condition to be created.

### `forceLBC` @type(FORCE\_LBC) @default(FORCE\_LBC)

- The general force parameters.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of targets for general force. This targets can be Face, Edge or Node.

### `crEdit` @type(Cursor) @default(None)

- An existing general force.
  - If this parameter is used, the specified general force will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new general force will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6,7}
Geometry.Part.Cube()

created_bcs = BoundaryConditions.Force.General(strName="Force1",
                                               forceLBC=FORCE_LBC(vecForce=[1.0,
                                                                            DFLT_DBL, 
                                                                            DFLT_DBL]),
                                               crlTargets=[Face(23)])

JPT.Debugger(created_bcs)
```
