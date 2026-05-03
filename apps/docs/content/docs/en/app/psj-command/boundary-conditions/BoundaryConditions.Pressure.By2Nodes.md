---
title: "BoundaryConditions.Pressure.By2Nodes()"
description: "Create load boundary condition of 2nodes pressure"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Pressure > By2Nodes"
---

## Description

Create load boundary condition of 2nodes pressure.

## Syntax

```psj
BoundaryConditions.Pressure.By2Nodes(...)
```

## Inputs

### `strName` @type(String) @default("PressureLinear1")

- The name.

### `crNodeA` @type(Cursor) @default(None)

- The node a.

### `dPressureA` @type(Double) @default(0.0)

- The pressure a.

### `iNodeAUnit` @type(Integer) @default(0)

- The node a unit.

### `crNodeB` @type(Cursor) @default(None)

- The node .

### `dPressureB` @type(Double) @default(0.0)

- The pressure .

### `iNodeBUnit` @type(Integer) @default(0)

- The node unit.

### `iDirection` @type(Integer) @default(0)

- The direction.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Pressure.By2Nodes(strName="PressureLinear1", crNodeA=None, dPressureA=0.0, iNodeAUnit=0, crNodeB=None, dPressureB=0.0, iNodeBUnit=0, iDirection=0, crlTargets=[], crEdit=None)
```
