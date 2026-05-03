---
title: "Connections.RigidElements.RBar.OneToOneNodesWithTolerance()"
description: "Create one-to-one (master:slave) RBar (rigid elements) with nodes tolerance"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBar > OneToOneNodesWithTolerance"
macro_link: "[RBarOneToOneNodesWithTolerance](../../macro/connections/RBarOneToOneNodesWithTolerance)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create RBar","Create one-to-one (master:slave) RBar (rigid elements) with nodes tolerance"]}
   [param_removed_unexpectedly] Param 'crlMasterTargets' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [param_removed_unexpectedly] Param 'crlSlaveTargets' last seen in v5.0.1 — no rename candidate found
     context: {"lastSeen":"5.0.1"}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create one-to-one (master:slave) RBar (rigid elements) with nodes tolerance.

## Syntax

```psj
Connections.RigidElements.RBar.OneToOneNodesWithTolerance(...)
```

## Inputs

### `strName` @type(String) @default("RBAR\_1")

- The RBar name to be created.

<!-- ### `crlMasterTargets`

- A _List of Cursor_ specifying the master target. Master target can be selected by node only.
- The default value is [].

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target. Slave target can be selected by node only.
- The default value is []. -->

### `crlTargets` @type(List\[Cursor]) @default(\[]) @since(5.1.0)

- The target nodes.

### `iMethod` @type(Integer) @default(21)

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

### `crlMasterTargets` @type(List\[Cursor]) @default(\[]) @deprecated @until(5.1.0)

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[]) @deprecated @until(5.1.0)

- The slave target.

## Return Code

A _Cursor_ specifying the created Rbar.

## Sample Code

```psj {6-9}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbar_connection = Connections.RigidElements.RBar.OneToOneNodesWithTolerance(strName="RBar_1", 
                                                                            crlTargets =[Node(493, 6, 496, 7)], 
                                                                            iUlDOFs=63, 
                                                                            dTol=0.005)
JPT.Debugger(rbar_connection)
```
