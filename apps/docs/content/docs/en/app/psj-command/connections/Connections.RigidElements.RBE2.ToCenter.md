---
title: "Connections.RigidElements.RBE2.ToCenter()"
description: "Create one-to-many (master:slave) RBE2 (rigid element)"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > RigidElements > RBE2 > ToCenter"
macro_link: "[RBE2ToCenter](../../macro/connections/RBE2ToCenter)"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["create RBE2","Create one-to-many (master:slave) RBE2 (rigid element)"]}
   [param_rename_candidate] 'iEnableCheckDuplicate' may be a rename of 'iEnableCheckDulplicate' (95% similar)
     context: {"from":"iEnableCheckDulplicate","to":"iEnableCheckDuplicate","similarity":0.9545454545454546}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create one-to-many (master:slave) RBE2 (rigid element).

## Syntax

```psj
Connections.RigidElements.RBE2.ToCenter(...)
```

## Inputs

### `iMethod` @type(Integer) @default(18)

- The connection method.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The master target.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The slave target. Slave target can be selected by part, face, edge, element, or node.

### `iEType` @type(Integer) @default(2)

- The connection type.

### `strName` @type(String) @default("RBE2\_1")

- The RBE2 name to be created.

### `crCoordSys` @type(Cursor) @default(None)

- The coordinate system.

### `dTolerance` @type(Double) @default(0.0)

- The tolerance.

### `iUlDOFs` @type(Integer) @default(63)

- The component of dependent degrees of freedom.

### `dlVirtualNodePos` @type(Double List) @default(\[0, 0, 0])

- The position of master node.

### `iSurfaceDef` @type(Integer) @default(0)

- The surface definition.
  - 0: By Node Set - Specify the node as a reference surface.
  - 1: By Element Set - Specify the element as a reference surface. Cannot configure an element to the slave entity (node, edge) and if it has been selected an error will be output.

### `crEdit` @type(Cursor) @default(None)

- An existing RBE2 connection
  - If this parameter is used, the specified RBE2 connection will be modified.
  - If it is left None, a new RBE2 will be created.

### `iEnableUpdateDispCS` @type(Integer) @default(1)

- Whether to update displacement coordinate system.

### `iEnableCornerOnly` @type(Integer) @default(0)

- Whether to connect only to the corner nodes of the selected entity.

### `iEnableCheckDuplicate` @type(Integer) @default(1) @since(5.1.0)

- Whether to check for duplicate.

### `iDuplicateMode` @type(Integer) @default(0)

- The duplicate mode.

### `iEnableCheckDulplicate` @type(Integer) @default(1) @deprecated @until(5.1.0)

- The enable check dulplicate.

## Return Code

A _Cursor_ specifying the created RBE2.

## Sample Code

```psj {6,7}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=7463537)

# Create the connections
rbe2_connection = Connections.RigidElements.RBE2.ToCenter(crlSlaveTargets=[Node(496, 493, 489, 492, 7, 6, 2, 3)], 
                                         iUlDOFs=45, dlVirtualNodePos=[0.015, 0.005, 0.005], iEnableCornerOnly=1)
JPT.Debugger(rbe2_connection)
```
