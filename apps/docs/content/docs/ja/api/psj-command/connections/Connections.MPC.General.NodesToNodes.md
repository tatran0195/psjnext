---
title: "Connections.MPC.General.NodesToNodes()"
description: "Create MPC between selected nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MPC > General > NodesToNodes"
macro _link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between selected nodes.

## Syntax

```psj
Connections.MPC.General.NodesToNodes(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the MPC name.
- The default value is "MPC\_1".

<!-- @since:5.0.1 @optional -->
### crlMasterNodes

- Specify the list of master nodes.
- In case this list has more than one selected node, the number of master nodes and slave nodes must be equal. The MPC is created by connecting selected master nodes with selected slave nodes one-to-one correspondingly.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### crlSlaveNodes

- Specify the list of slave nodes.
- In case this list has more than one selected node, the number of slave nodes and master nodes must be equal. The MPC is created by connecting selected master nodes with selected slave nodes correspondingly.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### listMpcConnection

- Specify the pair of MPC connection data type.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dSearchTol

- Specify the MPC search tolerance value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### dValue

- Specify the MPC value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iMPCType

- Specify the MPC type.
  - 0: MPC General.
  - 1: MPC Equation.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iSearchType

- Specify the search type.
- The default value is 1.

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

- Specify the exist MPC for editing.
  - If this parameter is used, the specified exist MPC item will be modified.
  - If it is left _None_, a new MPC item will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=12867524)

created _mpc = Connections.MPC.General.NodesToNodes(strName="MPC _5", 
                                                   crlMasterNodes=[Node(760, 
                                                                        770)],
                                                   crlSlaveNodes=[Node(323, 
                                                                       310)], 
                                                   listMpcConnection=[MPC _CONNECTION(dCoef=1.0, 
                                                                                     iDof=1),
                                                                      MPC _CONNECTION(dCoef=1.0, 
                                                                                     iDof=2), 
                                                                      MPC _CONNECTION(dCoef=1.0, 
                                                                                     iDof=4), 
                                                                      MPC _CONNECTION(),
                                                                      MPC _CONNECTION(), 
                                                                      MPC _CONNECTION()], 
                                                   bUpdateDispCS=1)
    
JPT.Debugger(created _mpc)
```
