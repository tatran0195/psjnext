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

<!-- @since:5.0.1 @optional -->
### strName

- Specify the MPC name.
- The default value is "MPC\_1".

<!-- @since:5.0.1 @optional -->
### crlMasterEntities

- Specify the list of master entities. The entities could be any of types such as Parts/Faces/Edges/Nodes.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### crlSlaveEntities

- Specify the list of slave entities. The entities could be any of types such as Parts/Faces/Edges/Nodes.
- This is the required input.

<!-- @since:5.0.1 @optional -->
### listMpcConnection

- Specify the list of MPC connection.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dConstantValue

- Specify the MPC value.
- The default value is 0.0.

<!-- @since:5.0.1 @optional -->
### iLocalCoordinate

- Specify the coordinate system.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### bUpdateDispCS

- Specify whether or not update displacement coordinate system.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### crMpcConnection

- Specify an existing contact setting (MPC Equation). If this parameter is used, the specified contact setting (MPC Equation) will be modified. When the default value is used, a new contact setting (MPC Equation) will be created.
- The default value is _None_.

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
