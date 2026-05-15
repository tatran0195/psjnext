---
title: "Connections.RigidElements.RBar.OneToOneNodesWithTolerance()"
description: "Create one-to-one (master:slave) RBar (rigid elements) with nodes tolerance"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBar > OneToOneNodesWithTolerance"
macro _link: "[RBarOneToOneNodesWithTolerance](../../macro/connections/RBarOneToOneNodesWithTolerance)"
---

## Description

Create one-to-one (master:slave) RBar (rigid elements) with nodes tolerance.

## Syntax

```psj
Connections.RigidElements.RBar.OneToOneNodesWithTolerance(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the RBar name to be created.
- The default value is "RBAR\_1".

<!-- ### `crlMasterTargets`

- A _List of Cursor_ specifying the master target. Master target can be selected by node only.
- The default value is [].

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target. Slave target can be selected by node only.
- The default value is []. -->

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify the target nodes.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iMethod

- Specify the connection method.
- The default value is 21.

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
  - If it is left None, a new Rbar will be created.
- The default value is _None_.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### crlMasterTargets

- Specify the master target.
- The default value is \[].

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### crlSlaveTargets

- Specify the slave target.
- The default value is \[].

## Return Code

A _Cursor_ specifying the created Rbar.

## Sample Code

```psj {6-9}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], strName="Cube _2", iPartColor=7463537)

# Create the connections
rbar _connection = Connections.RigidElements.RBar.OneToOneNodesWithTolerance(strName="RBar _1", 
                                                                            crlTargets =[Node(493, 6, 496, 7)], 
                                                                            iUlDOFs=63, 
                                                                            dTol=0.005)
JPT.Debugger(rbar _connection)
```
