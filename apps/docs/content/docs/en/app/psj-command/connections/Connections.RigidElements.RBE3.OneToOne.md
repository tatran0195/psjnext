---
title: "Connections.RigidElements.RBE3.OneToOne()"
description: "Create one to one (Slave:Master) RBE3 (Interpolation constraining Element)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBE3 > OneToOne"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create RBE3","Create one to one (Slave:Master) RBE3 (Interpolation constraining Element)"]}
   [param_removed_unexpectedly] Param 'iEnableUpdateDispCS' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'iEnableCornerOnly' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create one to one (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.OneToOne(...)
```

## Inputs

### `iMethod` @type(Integer) @default(17)

- The method.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target.

### `listRbe3TermConnection` @type(RBE3TERM\_CONNECTION List) @default(\[])

- The rbe3 term connection.

### `iTypeRBE3` @type(Integer) @default(3)

- The type r e3.

### `strName` @type(String) @default("")

- The name.

### `crCoordSys` @type(Cursor) @default(None)

- The coordinate system.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance.

### `dlVirtualNodePos` @type(Double List) @default(\[0, 0, 0])

- The virtual node position.

### `iSurfaceDef` @type(Integer) @default(0)

- The surface definition.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `bUpdateDispCS` @type(Boolean) @default(True) @since(5.1.0)

- The enable update displacement coordinate system.

### `iEnableUpdateDispCS` @type(Integer) @default(True) @deprecated @until(5.1.0)

- The enable update displacement coordinate system.

### `iEnableCornerOnly` @type(Integer) @default(False) @deprecated @until(5.1.0)

- The enable corner only.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {11-15}
Geometry.Part.Cube(
    ilAxialNodes=[4, 4, 4], strName="Cube_2", iPartColor=14903267)

Geometry.Part.Cube(
    dlOrigin=[0.012, 0.0, 0.0], 
    ilAxialNodes=[4, 4, 4], 
    strName="Cube_3", 
    iPartColor=7829501)

Connections.RigidElements.RBE3.OneToOne(
    crlMasterTargets=[Node(61, 87, 88, 64, 57, 71, 72, 60)], 
    crlSlaveTargets=[Node(6, 27, 28, 7, 2, 11, 12, 3)],
     listRbe3TermConnection=[(0, 63, 8), (1, 7, 8)],
     strName="RBE3_3")
```
