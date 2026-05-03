---
title: "BoundaryConditions.InitialNodalValue.RotationAngle()"
description: "Create initial rotation angle"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > RotationAngle"
---

## Description

Create initial rotation angle.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.RotationAngle(...)
```

## Inputs

### `strName` @type(String) @default("InitialVelocity1")

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
BoundaryConditions.InitialNodalValue.RotationAngle(strName="InitialVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTargets=[], crEdit=None)
```
