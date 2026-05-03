---
title: "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus()"
description: "Create initial angular velocity for the Abaqus solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > InitialAngularVelocity > Abaqus"
---

## Description

Create initial angular velocity for the Abaqus solver.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(...)
```

## Inputs

### `strName` @type(String) @default("InitialAngularVelocityAbaqus1")

- The name.

### `dVelocity` @type(Double) @default(DFLT\_DBL)

- The velocity.

### `strFirstCoord` @type(String) @default("")

- The first coordinate.

### `strSecondCoord` @type(String) @default("")

- The second coordinate.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(strName="InitialAngularVelocityAbaqus1", dVelocity=DFLT_DBL, strFirstCoord="", strSecondCoord="", crlTargets=[], crEdit=None)
```
