---
title: "Connections.MPC.General.NodeToFaces()"
description: "Create a MPC between a node and multiple faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MPC > General > NodeToFaces"
macro _link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create a MPC between a node and multiple faces.

## Syntax

```psj
Connections.MPC.General.NodeToFaces(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"MPC _1" -->
### `strName`

- The MPC name.

<!-- @since:5.0.1 @type:Cursor @optional -->
### `crMasterNode`

- The unique master node which needs to be connected.
- This is the required input.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlSlaveFaces`

- The list of slave faces which need to be connected. The master node will connect to all nodes on the edges of slave faces.
- This is the required input.

<!-- @since:5.0.1 @type:List[MPC _CONNECTION] @optional @default:[] -->
### `listMpcConnection`

- The list of MPC connection.

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

```psj {6,7,8,9,10,11,12,13,14,15}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=12867524)

created _mpc = Connections.MPC.General.NodeToFaces(strName="MPC _9", 
                                                  crMasterNode=Node(758),
                                                  crlSlaveFaces=[Face(24)], 
                                                  listMpcConnection=[MPC _CONNECTION(iDof=1), 
                                                                     MPC _CONNECTION(iDof=2),
                                                                     MPC _CONNECTION(iDof=4), 
                                                                     MPC _CONNECTION(), 
                                                                     MPC _CONNECTION(), 
                                                                     MPC _CONNECTION()],
                                                  bUpdateDispCS=1)

JPT.Debugger(created _mpc)
```
