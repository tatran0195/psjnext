---
title: "Connections.RigidElements.RBar.OneToOne()"
description: "Create one-to-one (master:slave) RBar (rigid elements)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBar > OneToOne"
macro_link: "[RBarOneToOne](../../macro/connections/RBarOneToOne)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create RBar","Create one-to-one (master:slave) RBar (rigid elements)"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create one-to-one (master:slave) RBar (rigid elements).

## Syntax

```psj
Connections.RigidElements.RBar.OneToOne(...)
```

## Inputs

### `strName` @type(String) @default("RBAR\_1")

- The RBar name to be created.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target. Master target can be selected by part, face, edge, element, or node.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target. Slave target can be selected by part, face, edge, element, or node.

### `iMethod` @type(Integer) @default(17)

- The connection method.

### `iUlDOFs` @type(Integer) @default(0)

- The master degrees of freedom. This function only support case where all components of the independent degrees of freedom are fixed for the nodes selected in the master.

### `dTol` @type(Double) @default(DFLT\_DBL)

- The tolerance.

### `crCoord` @type(Cursor) @default(None)

- The coordinate system.

### `bUpdateDispCS` @type(Boolean) @default(True) @since(5.1.0)

- Whether or not update displacement coordinate system.
  - If True, the displacement coordinate system is updated.
  - If False, displacement coordinate system is not updated.

### `crEdit` @type(Cursor) @default(None)

- An existing Rbar
  - If this parameter is used, the specified Rbar will be modified.
  - If it is left None, a new Rbar will be created.

## Return Code

A _Cursor_ specifying the created Rbar.

## Sample Code

```psj {6,7}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbar_connection = Connections.RigidElements.RBar.OneToOne(strName="RBar_1", crlMasterTargets=[Node(496)], 
                                    crlSlaveTargets=[Node(7)], iUlDOFs=63, dTol=0.0, bUpdateDispCS=True)
JPT.Debugger(rbar_connection)
```
