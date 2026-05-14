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

<!-- @since:5.0.1 @type:String @optional @default:"MPC _1" -->
### `strName`

- The MPC name.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMasterFace`

- The face to be master. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crSlaveFace`

- The face to be  slave. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.

<!-- @since:5.0.1 @type:List[MPC _CONNECTION] @optional @default:[] -->
### `listMpcConnection`

- The pair of MPC connection data type.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dValue`

- The MPC constant value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalCoordinate`

- The local coordinate system.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- Whether to change the Displacement Coordinate system at nodes belongs to selected faces to the specified local coordinate system.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMPCConnection`

- An existing MPC Connection (2 Faces). If this argument is not _None_, the specified MPC Connection will be modified. Otherwise, a new MPC Connection will be created. The couple _crMasterFace_, _crSlaveFace_ and _crMPCConnection_ arguments are mutually exclusive. One of them must be specified.

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
