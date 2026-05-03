---
title: "Connections.SpringsDampers.Spring.OneToOne.sameDoFs()"
description: "Spring connection One to One same DOFs"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > SpringsDampers > Spring > OneToOne > sameDoFs"
---

## Description

Spring connection One to One same DOFs

## Syntax

```psj
Connections.SpringsDampers.Spring.OneToOne.sameDoFs(iMethod=0, strName="SPRING", crlMasterTargets=[], crlSlaveTargets=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)
```

## Inputs

### `iMethod` @type(Integer) @default(0)

- The method.

### `strName` @type(String) @default("SPRING")

- The name.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(Cursor List) @default(\[])

- The slave target.

### `crCoordSys` @type(Cursor) @default(None)

- The coordinate system.

### `iSpringType` @type(Integer) @default(0)

- The spring type.

### `iGround` @type(Integer) @default(0)

- The ground.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance.

### `iDirection` @type(Integer) @default(0)

- The direction.

### `iDistributeMode` @type(Integer) @default(0)

- The distribute mode.

### `iDof1` @type(Integer) @default(0)

- The DOF 1.

### `iDof2` @type(Integer) @default(0)

- The DOF 2.

### `dDampCoef` @type(Double) @default(DFLT\_DBL)

- The damp coefficient .

### `dStressCoef` @type(Double) @default(DFLT\_DBL)

- The stress coefficient .

### `posTStiffness` @type(Position) @default(\[0,0,0])

- The t stiffness.

### `posRStiffness` @type(Position) @default(\[0,0,0])

- The r stiffness.

### `bUpdateDispCS` @type(Boolean) @default(True)

- The update displacement coordinate system.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.SpringsDampers.Spring.OneToOne.sameDoFs(iMethod=0, strName="SPRING", crlMasterTargets=[], crlSlaveTargets=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)
```
