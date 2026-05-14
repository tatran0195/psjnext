---
title: "Connections.RigidElements.RigidBodyConstraint.Nodes()"
description: "Create Rigid Body Constraint (LS-DYNA)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > RigidElements > RigidBodyConstraint > Nodes"
macro _link: ""
---

## Description

Create Rigid Body Constraint (LS-DYNA)

## Syntax

```psj
Connections.RigidElements.RigidBodyConstraint.Nodes(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"RBC" -->
### `strName`

- The name of Rigid Body Constraint.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iMethod`

- The method. Is is set 3 for this function.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlMasters`

- The master entities.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlSlaves`

- The slave entities.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- The existing Rigid Body Constraint.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-6}
Geometry.Part.Cube()
Connections.RigidElements.RigidBodyConstraint.Nodes(
    strName="RBC _1", 
    iMethod=3, 
    crlMasters=[Edge(15)])
```
