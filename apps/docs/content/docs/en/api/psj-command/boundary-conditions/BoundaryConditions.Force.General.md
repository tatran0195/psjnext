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

<!-- @since:5.0.1 @type:String @optional @default:"Force1" -->
### `strName`

- The name of force condition to be created.

<!-- @since:5.0.1 @type:FORCE _LBC @optional @default:FORCE _LBC -->
### `forceLBC`

- The general force parameters.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The list of targets for general force. This targets can be Face, Edge or Node.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing general force.
  - If this parameter is used, the specified general force will be modified.
  - If it is left _None_, a new general force will be created.

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
