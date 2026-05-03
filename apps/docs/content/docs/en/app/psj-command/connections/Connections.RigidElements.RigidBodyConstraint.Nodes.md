---
title: "Connections.RigidElements.RigidBodyConstraint.Nodes()"
description: "Create Rigid Body Constraint (LS-DYNA)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Connections > RigidElements > RigidBodyConstraint > Nodes"
macro_link: ""
---

## Description

Create Rigid Body Constraint (LS-DYNA)

## Syntax

```psj
Connections.RigidElements.RigidBodyConstraint.Nodes(...)
```

## Inputs

### `strName` @type(String) @default("RBC")

- The name of Rigid Body Constraint.

### `iMethod` @type(Integer) @default(0)

- Method. Is is set 3 for this function.

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
Connections.RigidElements.RigidBodyConstraint.Nodes(
    strName="RBC_1", 
    iMethod=3, 
    crlMasters=[Edge(15)])
```
