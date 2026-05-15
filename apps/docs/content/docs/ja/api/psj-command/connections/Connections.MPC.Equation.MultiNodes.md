---
title: "Connections.MPC.Equation.MultiNodes()"
description: "Create a MPC connection between a slave node with multi-master nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MPC > Equation > MultiNodes"
macro _link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create a MPC connection between a slave node with multi-master nodes.

## Syntax

```psj
Connections.MPC.Equation.MultiNodes(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the MPC name.
- The default value is "MPC\_1".

<!-- @since:5.0.1 @optional -->
### crlMasterNodes

- Specify the list of master nodes which need to be connected. The master nodes are the nodes from the second selected node onwards in the selection list of nodes.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### crSlaveNode

- Specify the slave node which needs to be connected. The slave node is the first selected node in the selection list of nodes. This slave node will connect to all master nodes.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### listMpcConnection

- Specify the list of MPC connection.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dValue

- Specify the MPC value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iLocalCoordinate

- Specify the local coordinate system.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bUpdateDispCS

- Specify whether or not update displacement coordinate system.
  - If _True_, the displacement coordinate system is updated.
  - If _False_, displacement coordinate system is not updated.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### crMPCConnection

- Specify an existing MPC connection.
  - If this parameter is used, the specified MPC connection will be modified.
  - If it is left _None_, a new MPC connection will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16,17,18}
Geometry.Part.Cube(iPartColor = 7666683)
Geometry.Part.Cube(dlOrigin = [0.02, 0.0, 0.0], 
                   strName = "Cube _2", 
                   iPartColor = 12867524)

created _mpc = Connections.MPC.Equation.MultipleNodes(crlMasterNodes=[Node(340,
                                                                          344, 
                                                                          353)],
                                                     crSlaveNode=Node(757), 
                                                     listMpcConnection=[MPC _CONNECTION(dCoef=1.0, 
                                                                                       iDof=1),
                                                                        MPC _CONNECTION(dCoef=1.0, 
                                                                                       iDof=1), 
                                                                        MPC _CONNECTION(dCoef=1.0, 
                                                                                       iDof=1),
                                                                        MPC _CONNECTION(dCoef=1.0, 
                                                                                       iDof=1)], 
                                                     bUpdateDispCS=1)

JPT.Debugger(created _mpc)
```
