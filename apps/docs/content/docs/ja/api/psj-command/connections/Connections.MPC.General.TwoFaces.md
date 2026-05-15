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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the MPC name.
- The default value is "MPC\_1".

<!-- @since:5.0.1 @optional -->
### crMasterFace

- Specify the master face. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crSlaveFace

- Specify the slave face. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### listMpcConnection

- Specify the pair of MPC connection data type.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### iLocalCoordinate

- Specify the local coordinate system.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bUpdateDispCS

- Specify whether or not update displacement coordinate system at nodes belongs to selected faces to the specified local coordinate system.
  - If _True_, the displacement coordinate system is updated.
  - If _False_, displacement coordinate system is not updated.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### crMPCConnection

- Specify the exist MPC for editing. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.
  - If this parameter is used, the specified exist MPC item will be modified.
  - If it is left _None_, a new MPC item will be created.
- The default value is _None_.

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
