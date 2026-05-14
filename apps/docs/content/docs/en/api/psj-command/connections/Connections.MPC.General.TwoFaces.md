---
title: "Connections.MPC.General.TwoFaces()"
description: "Create MPC between two faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MPC > General > TwoFaces"
macro _link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between two faces.

## Syntax

```psj
Connections.MPC.General.TwoFaces(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"MPC _1" -->
### `strName`

- The MPC name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMasterFace`

- The master face. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSlaveFace`

- The slave face. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:List[MPC _CONNECTION] @optional @default:[] -->
### `listMpcConnection`

- The pair of MPC connection data type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalCoordinate`

- The local coordinate system.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- Whether or not update displacement coordinate system at nodes belongs to selected faces to the specified local coordinate system.
  - If _True_, the displacement coordinate system is updated.
  - If _False_, displacement coordinate system is not updated.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMPCConnection`

- The exist MPC for editing. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.
  - If this parameter is used, the specified exist MPC item will be modified.
  - If it is left _None_, a new MPC item will be created.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection (2 Faces).

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=12867524)

created _mpc = Connections.MPC.General.TwoFaces(strName="MPC _12", 
                                               crMasterFace=Face(49),
                                               crSlaveFace=Face(24), 
                                               listMpcConnection=[MPC _CONNECTION(iDof=1), 
                                                                  MPC _CONNECTION(iDof=2),
                                                                  MPC _CONNECTION(iDof=4), 
                                                                  MPC _CONNECTION(), 
                                                                  MPC _CONNECTION(),
                                                                  MPC _CONNECTION()], 
                                               bUpdateDispCS=1)

JPT.Debugger(created _mpc)
```
