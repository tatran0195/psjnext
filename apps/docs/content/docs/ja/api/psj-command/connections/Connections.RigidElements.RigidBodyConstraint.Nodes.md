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

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of Rigid Body Constraint.
- The default value is "RBC".

<!-- @since:5.1.0 @optional -->
### iMethod

- Specify method. Is is set 3 for this function.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### crlMasters

- Specify master entities.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crlSlaves

- Specify slave entities.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify existing Rigid Body Constraint.
- The default value is _None_.

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
