---
title: "Connections.RigidElements.RigidBodyConstraint.NodesToBody()"
description: "Create Rigid Body Constraint (LS-DYNA)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Connections > RigidElements > RigidBodyConstraint > NodesToBody"
macro_link: ""
---

## Description

Create Rigid Body Constraint (LS-DYNA)

## Syntax

```psj
Connections.RigidElements.RigidBodyConstraint.NodesToBody(...)
```

## Inputs

### `strName` @type(String) @default("RBC")

- The name of Rigid Body Constraint.

### `iMethod` @type(Integer) @default(0)

- Type.
  - 1: Node.
  - 2: Node set.

### `crlMasters` @type(List\[Cursor]) @default(\[])

- Master entities.

### `crlSlaves` @type(List\[Cursor]) @default(\[])

- Slave entities.

### `crEdit` @type(Cursor) @default(None)

- Existing Rigid Body Constraint.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {2-6}
Geometry.Part.Cube()
Connections.RigidElements.RigidBodyConstraint.NodesToBody(
    strName="RBC_1", 
    iMethod=1, 
    crlMasters=[Part(1)], 
    crlSlaves=[Node(460)])
```
