---
title: "BoundaryConditions.Force.General()"
description: "Create a general force applied to the selected Face, Edge or Node. User inputs the force values and it will apply the force to the selected items"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > Force > General"
---

## Description

Create a general force applied to the selected Face, Edge or Node. User inputs the force values and it will apply the force to the selected items.

## Syntax

```psj
BoundaryConditions.Force.General(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of force condition to be created.
- The default value is "Force1".

<!-- @since:5.0.1 @optional -->
### forceLBC

- Specify the general force parameters.
- The default value is _[FORCE\_LBC](./../../data-type/psj-command/parameter-types/FORCE _LBC)_.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of targets for general force. This targets can be Face, Edge or Node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing general force.
  - If this parameter is used, the specified general force will be modified.
  - If it is left _None_, a new general force will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6,7}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.Force.General(strName="Force1",
                                               forceLBC=FORCE _LBC(vecForce=[1.0,
                                                                            DFLT _DBL, 
                                                                            DFLT _DBL]),
                                               crlTargets=[Face(23)])

JPT.Debugger(created _bcs)
```
