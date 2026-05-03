---
title: "BoundaryConditions.InitialNodalValue.Displacement()"
description: "Create Initial Dynamic"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > InitialNodalValue > Displacement"
---

## Description

Create Initial Dynamic.

## Syntax

```psj
BoundaryConditions.InitialNodalValue.Displacement(...)
```

## Inputs

### `strName` @type(String) @default("InitialDisplacement1")

- The name.

### `iType` @type(Integer) @default(0)

- The type.

### `vecInit` @type(Vector) @default(\[DFLT\_DBL,DFLT\_DBL,DFLT\_DBL])

- The initial.

### `bSelNode` @type(Boolean) @default(False)

- The selection node.

### `crNodeSet` @type(Cursor) @default(None)

- The node set.

### `crTable` @type(Cursor) @default(None)

- The table.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.InitialNodalValue.Displacement(strName="InitialDisplacement1", iType=0, vecInit=[DFLT_DBL,DFLT_DBL,DFLT_DBL], bSelNode=False, crNodeSet=None, crTable=None, crCoord=None, crlTargets=[], crEdit=None)
```
