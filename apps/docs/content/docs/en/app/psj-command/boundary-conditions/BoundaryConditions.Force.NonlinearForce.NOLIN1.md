---
title: "BoundaryConditions.Force.NonlinearForce.NOLIN1()"
description: "Create Nonlinear Force of NOLIN1(Table)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Force > NonlinearForce > NOLIN1"
---

## Description

Create Nonlinear Force of NOLIN1(Table).

## Syntax

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN1(...)
```

## Inputs

### `strName` @type(String) @default("NonlinearForce1\_1")

- The name.

### `dForceScale` @type(Double) @default(0.0)

- The force scale.

### `dMomentScale` @type(Double) @default(0.0)

- The moment scale.

### `iForcDir` @type(Integer) @default(0)

- The forc direction.

### `iForceDepends` @type(Integer) @default(0)

- The force depends.

### `iMomentDir` @type(Integer) @default(0)

- The moment direction.

### `iMomentDepends` @type(Integer) @default(0)

- The moment depends.

### `crCoord` @type(Cursor) @default(None)

- The coordinate.

### `crForceTable` @type(Cursor) @default(None)

- The force table.

### `crMomentTable` @type(Cursor) @default(None)

- The moment table.

### `crlMaster` @type(List\[Cursor]) @default(\[])

- The master.

### `crlSlave` @type(List\[Cursor]) @default(\[])

- The slave.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN1(strName="NonlinearForce1_1", dForceScale=0.0, dMomentScale=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCoord=None, crForceTable=None, crMomentTable=None, crlMaster=[], crlSlave=[], crEdit=None)
```
