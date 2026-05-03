---
title: "Connections.MPC.Equation.TwoFaces()"
description: "Create MPC between multiple points of two faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MPC > Equation > TwoFace"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between multiple points of two faces.

## Syntax

```psj
Connections.MPC.Equation.TwoFaces(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crMasterFace` @type(Cursor) @default(None)

- The face to be master. The coupl&#x65;_&#x63;rMasterFace_,_crSlaveFac&#x65;_&#x61;n&#x64;_&#x63;rMPCConnectio&#x6E;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `crSlaveFace` @type(Cursor) @default(None)

- The face to be  slave. The coupl&#x65;_&#x63;rMasterFace_,_crSlaveFac&#x65;_&#x61;n&#x64;_&#x63;rMPCConnectio&#x6E;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `listMpcConnection` @type(List\[MPC\_CONNECTION]) @default(\[])

- The pair of MPC connection data type.

### `dValue` @type(Double) @default(0.0)

- The MPC constant value.

### `iLocalCoordinate` @type(Integer) @default(0)

- The local coordinate system.

### `bUpdateDispCS` @type(Boolean) @default(True)

- Whether to change the Displacement Coordinate system at nodes belongs to selected faces to the specified local coordinate system.

### `crMPCConnection` @type(Cursor) @default(None)

- An existing MPC Connection (2 Faces). If this argument is no&#x74;_&#x4E;one_, the specified MPC Connection will be modified. Otherwise, a new MPC Connection will be created. The coupl&#x65;_&#x63;rMasterFace_,_crSlaveFac&#x65;_&#x61;n&#x64;_&#x63;rMPCConnectio&#x6E;_&#x61;rguments are mutually exclusive. One of them must be specified.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.Equation.TwoFaces(strName="MPC_1", 
                                                crMasterFace=Face(49), 
                                                crSlaveFace=Face(24),
                                                listMpcConnection=[MPC_CONNECTION(dCoef=1.0, 
                                                                                  iDof=1), 
                                                                   MPC_CONNECTION(dCoef=-1.0, 
                                                                                  iDof=1)], 
                                                bUpdateDispCS=1)

JPT.Debugger(created_mpc)
```
