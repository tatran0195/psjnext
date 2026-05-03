---
title: "BoundaryConditions.InitialNodalValue.Velocity()"
description: "Create initial velocity"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > Velocity"
---

## Description

Create initial velocity.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.Velocity(...)
```

## Inputs

### `strName` @type(String) @default("InitialRotationAngle1")

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
BoundaryConditions.InitialNodalValue.Velocity(strName="InitialRotationAngle1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTargets=[], crEdit=None)
```
