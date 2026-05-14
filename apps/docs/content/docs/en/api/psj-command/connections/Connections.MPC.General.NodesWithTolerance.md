---
title: "Connections.MPC.General.NodesWithTolerance()"
description: "Create a one-to-one MPC pair between multiple selected nodes within an arbitrary tolerance"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MPC > General > NodesWithTolerance"
macro _link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create a one-to-one MPC pair between multiple selected nodes within an arbitrary tolerance.

## Syntax

```psj
Connections.MPC.General.NodesWithTolerance(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"MPC _1" -->
### `strName`

- The MPC name.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlMasterNodes`

- The list of nodes which need to be connected.
- This is the required input.

<!-- @since:5.0.1 @type:List[MPC _CONNECTION] @optional @default:[] -->
### `listMpcConnection`

- The pair of MPC connection data type.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dSearchTol`

- The MPC search tolerance value.

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

created _mpc = Connections.MPC.General.NodesWithTolerance(strName="MPC _6",
                                                         crlMasterNodes=[Node(324, 766)], 
                                                         listMpcConnection=[MPC _CONNECTION(iDof=1),
                                                                            MPC _CONNECTION(iDof=2), 
                                                                            MPC _CONNECTION(iDof=4), 
                                                                            MPC _CONNECTION(), 
                                                                            MPC _CONNECTION(),
                                                                            MPC _CONNECTION()], 
                                                         dSearchTol=0.02, 
                                                         bUpdateDispCS=1)

JPT.Debugger(created _mpc)
```
