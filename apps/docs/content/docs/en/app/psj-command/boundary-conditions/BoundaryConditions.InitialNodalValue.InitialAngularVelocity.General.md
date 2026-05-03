---
title: "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General()"
description: "Create initial angular velocity for the general case"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > InitialAngularVelocity > General"
---

## Description

Create initial angular velocity for the general case.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General(...)
```

## Inputs

### `strName` @type(String) @default("InitialAngularVelocity1")

- The name.

### `stData` @type(ST\_DATA) @default(LBC\_DYNAMIC\_INITIAL\_CONDITION\_DATA())

- The data.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General(strName="InitialAngularVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTargets=[], crEdit=None)
```
