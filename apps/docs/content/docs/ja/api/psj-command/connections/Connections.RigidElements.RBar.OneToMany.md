---
title: "Connections.RigidElements.RBar.OneToMany()"
description: "Create one-to-many (master:slave) RBar (rigid elements)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBar > OneToMany"
macro _link: "[RBarOneToMany](../../macro/connections/RBarOneToMany)"
---

## Description

Create one-to-many (master:slave) RBar (rigid elements).

## Syntax

```psj
Connections.RigidElements.RBar.OneToMany(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the RBar name to be created.
- The default value is "RBAR\_1".

<!-- @since:5.0.1 @optional -->
### crlMasterTargets

- Specify the master target. Master target can be selected by part, face, edge, element, or node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crlSlaveTargets

- Specify the slave target. Slave target can be selected by part, face, edge, element, or node.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the connection method.
- The default value is 16.

<!-- @since:5.0.1 @optional -->
### iUlDOFs

- Specify the master degrees of freedom. This function only support case where all components of the independent degrees of freedom are fixed for the nodes selected in the master.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dTol

- Specify the tolerance.
- The default value is DFLT\_DBL.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate system.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bUpdateDispCS

- Specify whether or not update displacement coordinate system.
  - If True, the displacement coordinate system is updated.
  - If False, displacement coordinate system is not updated.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing Rbar
  - If this parameter is used, the specified Rbar will be modified.
  - If it is left None, a new RBar will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created Rbar.

## Sample Code

```psj {6,7}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=7463537)

# Create the connections
rbar _connection = Connections.RigidElements.RBar.OneToMany(strName="RBar _1", crlMasterTargets=[Node(496)], 
                                crlSlaveTargets=[Node(7, 85, 6)], iUlDOFs=63, dTol=0.0, bUpdateDispCS=True)
JPT.Debugger(rbar _connection)
```
