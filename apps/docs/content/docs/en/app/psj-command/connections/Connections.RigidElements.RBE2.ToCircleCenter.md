---
title: "Connections.RigidElements.RBE2.ToCircleCenter()"
description: "create RBE2"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBE2 > ToCircleCenter"
---
<!-- REVIEW FLAGS — requires human review
   [param_rename_candidate] 'iEnableCheckDuplicate' may be a rename of 'iEnableCheckDulplicate' (95% similar)
     context: {"from":"iEnableCheckDulplicate","to":"iEnableCheckDuplicate","similarity":0.9545454545454546}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create RBE2

## Syntax

```psj
Connections.RigidElements.RBE2.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)
```

## Inputs

### `iMethod` @type(Integer) @default(19)

- The method.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target.

### `iEType` @type(Integer) @default(2)

- The e type.

### `strName` @type(String) @default("RBE2\_1")

- The name.

### `crCoordSys` @type(Cursor) @default(None)

- The coordinate system.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance.

### `iUlDOFs` @type(Integer) @default(63)

- The ul d o fs.

### `dlVirtualNodePos` @type(Double List) @default(\[0, 0, 0])

- The virtual node position.

### `iSurfaceDef` @type(Integer) @default(0)

- The surface definition.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iEnableUpdateDispCS` @type(Integer) @default(1)

- The enable update displacement coordinate system.

### `iEnableCornerOnly` @type(Integer) @default(0)

- The enable corner only.

### `iEnableCheckDuplicate` @type(Integer) @default(1) @since(5.1.0)

- The enable check dulplicate.

### `iDuplicateMode` @type(Integer) @default(0)

- The duplicate mode.

### `iEnableCheckDulplicate` @type(Integer) @default(1) @deprecated @until(5.1.0)

- The enable check dulplicate.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.RigidElements.RBE2.ToCircleCenter(iMethod=19, crlMasterTargets=[], crlSlaveTargets=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)
```
