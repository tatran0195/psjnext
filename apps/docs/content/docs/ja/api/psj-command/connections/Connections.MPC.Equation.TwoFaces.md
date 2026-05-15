---
title: "Connections.MPC.Equation.TwoFaces()"
description: "Create MPC between multiple points of two faces"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MPC > Equation > TwoFace"
macro _link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between multiple points of two faces.

## Syntax

```psj
Connections.MPC.Equation.TwoFaces(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the MPC name.
- The default value is "MPC\_1".

<!-- @since:5.0.1 @optional -->
### crMasterFace

- Specify the face to be master. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### crSlaveFace

- Specify the face to be  slave. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

<!-- @since:5.0.1 @optional -->
### listMpcConnection

- Specify the pair of MPC connection data type.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dValue

- Specify the MPC constant value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iLocalCoordinate

- Specify the local coordinate system.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bUpdateDispCS

- Specify whether to change the Displacement Coordinate system at nodes belongs to selected faces to the specified local coordinate system.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### crMPCConnection

- Specify an existing MPC Connection (2 Faces). If this argument is not _None_, the specified MPC Connection will be modified. Otherwise, a new MPC Connection will be created. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=12867524)

created _mpc = Connections.MPC.Equation.TwoFaces(strName="MPC _1", 
                                                crMasterFace=Face(49), 
                                                crSlaveFace=Face(24),
                                                listMpcConnection=[MPC _CONNECTION(dCoef=1.0, 
                                                                                  iDof=1), 
                                                                   MPC _CONNECTION(dCoef=-1.0, 
                                                                                  iDof=1)], 
                                                bUpdateDispCS=1)

JPT.Debugger(created _mpc)
```
