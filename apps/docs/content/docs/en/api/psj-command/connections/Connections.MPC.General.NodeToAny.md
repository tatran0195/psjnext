---
title: "Connections.MPC.General.NodeToAny()"
description: "Create MPC between a selected node and any types of entities such as nodes, edges or faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MPC > General > NodeToAny"
macro _link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between a selected node and any types of entities such as nodes, edges or faces.

## Syntax

```psj
Connections.MPC.General.NodeToAny(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"MPC _1" -->
### `strName`

- The MPC name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMasterNode`

- The master node which needs to be connected.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlSlaveEntities`

- The list of slave entities such as nodes, edges or faces which need to be connected. The slave entities list can contain different types of entities at the same time.
- This is the required input.

<!-- @since:5.0.1 @type:List[MPC _CONNECTION] @optional @default:[] -->
### `listMpcConnection`

- The pair of MPC connection data type.

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

```psj {6,7,8,9,10,11,12,13,14,15,16}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=12867524)

created _mpc = Connections.MPC.General.NodeToAny(strName="MPC _7", 
                                                crMasterNode=Node(757),
                                                crlSlaveEntities=[Node(333), 
                                                                  Edge(14)], 
                                                listMpcConnection=[MPC _CONNECTION(iDof=1),
                                                                   MPC _CONNECTION(iDof=2), 
                                                                   MPC _CONNECTION(iDof=4), 
                                                                   MPC _CONNECTION(), 
                                                                   MPC _CONNECTION(),
                                                                   MPC _CONNECTION()], 
                                                bUpdateDispCS=1)
    
JPT.Debugger(created _mpc)
```
