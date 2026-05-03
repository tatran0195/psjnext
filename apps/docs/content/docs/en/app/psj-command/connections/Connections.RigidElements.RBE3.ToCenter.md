---
title: "Connections.RigidElements.RBE3.ToCenter()"
description: "Create one to many (Slave:Master) RBE3 (Interpolation constraining Element)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBE3 > ToCenter"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Create RBE3","Create one to many (Slave:Master) RBE3 (Interpolation constraining Element)"]}
   [param_removed_unexpectedly] Param 'iEnableUpdateDispCS' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'iEnableCornerOnly' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create one to many (Slave:Master) RBE3 (Interpolation constraining Element).

## Syntax

```psj
Connections.RigidElements.RBE3.ToCenter(...)
```

## Inputs

### `iMethod` @type(Integer) @default(18)

- The method.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target.

### `listRbe3TermConnection` @type(RBE3TERM\_CONNECTION List) @default(\[])

- The rbe3 term connection.

### `iTypeRBE3` @type(Integer) @default(3)

- The type rbe3.

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

### `bCornerOnly` @type(Boolean) @default(False) @since(5.1.0)

- The enable corner only.

### `iEnableUpdateDispCS` @type(Integer) @default(True) @deprecated @until(5.1.0)

- The enable update displacement coordinate system.

### `iEnableCornerOnly` @type(Integer) @default(False) @deprecated @until(5.1.0)

- The enable corner only.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj {3-6}
Geometry.Part.Cylinder(bHollow=True, dTopInnerRadius=0.005, dBottomInnerRadius=0.005, iPartColor=15658599)

Connections.RigidElements.RBE3.ToCenter(crlMasterTargets=[Edge(1)], 
                                    listRbe3TermConnection=[(0, 63, 1), (1, 7, 1)], 
                                    strName="RBE3_1", 
                                    dlVirtualNodePos=[0, 0.01, 0])
```
