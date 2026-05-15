---
title: "Connections.RigidElements.RigidBodyConstraint.NodesToBody()"
description: "Create Rigid Body Constraint (LS-DYNA)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Connections > RigidElements > RigidBodyConstraint > NodesToBody"
macro _link: ""
---

## Description

Create Rigid Body Constraint (LS-DYNA)

## Syntax

```psj
Connections.RigidElements.RigidBodyConstraint.NodesToBody(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of Rigid Body Constraint.
- The default value is "RBC".

<!-- @since:5.1.0 @optional -->
### iMethod

- Specify type.
  - 1: Node.
  - 2: Node set.
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
Connections.RigidElements.RigidBodyConstraint.NodesToBody(
    strName="RBC _1", 
    iMethod=1, 
    crlMasters=[Part(1)], 
    crlSlaves=[Node(460)])
```
