---
title: "Connections.MPC.Equation.SemiAuto()"
description: "Creates the MPC between the nodes with a distance tolerance"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MPC > Equation > SemiAuto"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Creates the MPC between the nodes with a distance tolerance.

## Syntax

```psj
Connections.MPC.Equation.SemiAuto(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crlMasterEntities` @type(List\[Cursor])

- The list of master entities. The entities could be any of types such as Parts/Faces/Edges/Nodes.
- This is the required input.

### `crlSlaveEntities` @type(List\[Cursor])

- The list of slave entities. The entities could be any of types such as Parts/Faces/Edges/Nodes.
- This is the required input.

### `listMpcConnection` @type(List\[MPC\_CONNECTION]) @default(\[])

- The list of MPC connection.

### `dConstantValue` @type(Double) @default(0.0)

- The MPC value.

### `iLocalCoordinate` @type(Integer) @default(0)

- The coordinate system.

### `bUpdateDispCS` @type(Boolean) @default(True)

- Whether or not update displacement coordinate system.

### `crMpcConnection` @type(Cursor) @default(None)

- An existing contact setting (MPC Equation). If this parameter is used, the specified contact setting (MPC Equation) will be modified. When the default value is used, a new contact setting (MPC Equation) will be created.

## Return Code

A _Cursor_ specifying the created or the modified contact connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.Equation.SemiAuto(crlMasterEntities=[Face(24)], 
                                                crlSlaveEntities=[Face(49)], 
                                                listMpcConnection=[MPC_CONNECTION(dCoef=20.0, 
                                                                                  iDof=1), 
                                                                   MPC_CONNECTION(dCoef=-20.0, 
                                                                                  iDof=1)], 
                                                dConstantValue=10.0, 
                                                bUpdateDispCS=1)

JPT.Debugger(created_mpc)
```
