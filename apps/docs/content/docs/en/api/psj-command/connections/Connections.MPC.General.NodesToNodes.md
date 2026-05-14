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

<!-- @since:5.0.1 @type:String @optional @default:"MPC _1" -->
### `strName`

- The MPC name.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlMasterNodes`

- The list of master nodes.
- In case this list has more than one selected node, the number of master nodes and slave nodes must be equal. The MPC is created by connecting selected master nodes with selected slave nodes one-to-one correspondingly.
- This is the required input.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlSlaveNodes`

- The list of slave nodes.
- In case this list has more than one selected node, the number of slave nodes and master nodes must be equal. The MPC is created by connecting selected master nodes with selected slave nodes correspondingly.
- This is the required input.

<!-- @since:5.0.1 @type:List[MPC _CONNECTION] @optional @default:[] -->
### `listMpcConnection`

- The pair of MPC connection data type.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSearchTol`

- The MPC search tolerance value.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dValue`

- The MPC value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMPCType`

- The MPC type.
  - 0: MPC General.
  - 1: MPC Equation.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iSearchType`

- The search type.

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

- The exist MPC for editing.
  - If this parameter is used, the specified exist MPC item will be modified.
  - If it is left _None_, a new MPC item will be created.

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
