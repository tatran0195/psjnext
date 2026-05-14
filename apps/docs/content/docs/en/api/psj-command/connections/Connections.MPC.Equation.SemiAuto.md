---
title: "Connections.MPC.Equation.SemiAuto()"
description: "Creates the MPC between the nodes with a distance tolerance"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > MPC > Equation > SemiAuto"
macro _link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Creates the MPC between the nodes with a distance tolerance.

## Syntax

```psj
Connections.MPC.Equation.SemiAuto(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"MPC _1" -->
### `strName`

- The MPC name.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlMasterEntities`

- The list of master entities. The entities could be any of types such as Parts/Faces/Edges/Nodes.
- This is the required input.

<!-- @since:5.0.1 @type:List[Cursor] @optional -->
### `crlSlaveEntities`

- The list of slave entities. The entities could be any of types such as Parts/Faces/Edges/Nodes.
- This is the required input.

<!-- @since:5.0.1 @type:List[MPC _CONNECTION] @optional @default:[] -->
### `listMpcConnection`

- The list of MPC connection.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dConstantValue`

- The MPC value.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iLocalCoordinate`

- The coordinate system.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- Whether or not update displacement coordinate system.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crMpcConnection`

- An existing contact setting (MPC Equation). If this parameter is used, the specified contact setting (MPC Equation) will be modified. When the default value is used, a new contact setting (MPC Equation) will be created.

## Return Code

A _Cursor_ specifying the created or the modified contact connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=12867524)

created _mpc = Connections.MPC.Equation.SemiAuto(crlMasterEntities=[Face(24)], 
                                                crlSlaveEntities=[Face(49)], 
                                                listMpcConnection=[MPC _CONNECTION(dCoef=20.0, 
                                                                                  iDof=1), 
                                                                   MPC _CONNECTION(dCoef=-20.0, 
                                                                                  iDof=1)], 
                                                dConstantValue=10.0, 
                                                bUpdateDispCS=1)

JPT.Debugger(created _mpc)
```
