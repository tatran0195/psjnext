---
title: "BoundaryConditions.Force.NonlinearForce.NOLIN4()"
description: "Create nonlinear force NOLIN4"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "BoundaryConditions > Force > NonlinearForce > NOLIN4"
---

## Description

Create nonlinear force NOLIN4.

## Syntax

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN4(...)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `dForceScale` @type(Double) @default(0.0)

- The force scale.

### `dMomentScale` @type(Double) @default(0.0)

- The moment scale.

### `dForcePowerA` @type(Double) @default(0.0)

- The force power a.

### `dMomentPowerA` @type(Double) @default(0.0)

- The moment power a.

### `iForcDir` @type(Integer) @default(0)

- The forc direction.

### `iForceDepends` @type(Integer) @default(0)

- The force depends.

### `iMomentDir` @type(Integer) @default(0)

- The moment direction.

### `iMomentDepends` @type(Integer) @default(0)

- The moment depends.

### `crCurCoord` @type(Cursor) @default(None)

- The cur coordinate.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
BoundaryConditions.Force.NonlinearForce.NOLIN4(strName, dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTargets=[], crlSlaveTargets=[], crEdit=None)
```
