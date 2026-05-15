---
title: "Connections.RigidElements.RBE2.OneToOne()"
description: "Create one-to-one (master:slave) RBE2 (rigid element)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE2 > OneToOne"
macro _link: "[RBE2OneToOne](../../macro/connections/RBE2OneToOne)"
---

## Description

Create one-to-one (master:slave) RBE2 (rigid element).

## Syntax

```psj
Connections.RigidElements.RBE2.OneToOne(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the connection method.
- The default value is 17.

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target. Master target can be selected by part, face, edge, element, or node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target. Slave target can be selected by part, face, edge, element, or node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iEType

- Specify the connection type.
- The default value is 2.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the RBE2 name to be created.
- The default value is "RBE2\_1".

<!-- @since:5.0.1 @optional -->
### crCoordSys

- Specify the coordinate system.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### dTolerance

- Specify the tolerance.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iUlDOFs

- Specify the component of dependent degrees of freedom.
- The default value is 63.

<!-- @since:5.0.1 @optional -->
<!-- @since:5.1.0 -->
### dlVirtualNodePos

- Specify the virtual node position.
- The default value is \[0, 0, 0].

<!-- @since:5.0.1 @optional -->
### iSurfaceDef

- Specify the surface definition.
  - 0: By Node Set - Specify the node as a reference surface.
  - 1: By Element Set - Specify the element as a reference surface. Cannot configure an element to the slave entity (node, edge) and if it has been selected an error will be output.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing RBE2 connection
  - If this parameter is used, the specified RBE2 connection will be modified.
  - If it is left None, a new RBE2 will be created.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### iEnableUpdateDispCS

- Specify whether to update displacement coordinate system.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iEnableCornerOnly

- Specify whether to connect only to the corner nodes of the selected entity.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iEnableCheckDuplicate

- Specify whether to check for duplicate.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iDuplicateMode

- Specify the duplicate mode.
- The default value is 0.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### iEnableCheckDulplicate

- Specify the enable check dulplicate.
- The default value is 1.

## Return Code

A _Cursor_ specifying the created RBE2.

## Sample Code

```psj {6,7}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=7463537)

# Create the connections
rbe2 _connection = Connections.RigidElements.RBE2.OneToOne(crlMasterTargets=[Node(496)], 
                                            crlSlaveTargets=[Node(7)], strName="RBE2 _3")
JPT.Debugger(rbe2 _connection)
```
