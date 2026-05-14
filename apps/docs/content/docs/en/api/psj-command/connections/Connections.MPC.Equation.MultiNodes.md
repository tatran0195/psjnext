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

<!-- @since:5.0.1 @type:String @optional @default:"MPC _1" -->
### `strName`

- The MPC name.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlMasterNodes`

- The list of master nodes which need to be connected. The master nodes are the nodes from the second selected node onwards in the selection list of nodes.
- This is the required input.

<!-- @since:5.0.1 @type:Cursor @optional -->
### `crSlaveNode`

- The slave node which needs to be connected. The slave node is the first selected node in the selection list of nodes. This slave node will connect to all master nodes.
- This is the required input.

<!-- @since:5.0.1 @type:List[MPC _CONNECTION] @optional @default:[] -->
### `listMpcConnection`

- The list of MPC connection.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dValue`

- The MPC value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalCoordinate`

- The local coordinate system.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- Whether or not update displacement coordinate system.
  - If _True_, the displacement coordinate system is updated.
  - If _False_, displacement coordinate system is not updated.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMPCConnection`

- An existing MPC connection.
  - If this parameter is used, the specified MPC connection will be modified.
  - If it is left _None_, a new MPC connection will be created.

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
