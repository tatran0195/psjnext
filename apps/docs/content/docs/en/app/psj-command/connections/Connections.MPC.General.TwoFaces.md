---
title: "Connections.MPC.General.TwoFaces()"
description: "Create MPC between two faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MPC > General > TwoFaces"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between two faces.

## Syntax

```psj
Connections.MPC.General.TwoFaces(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crMasterFace` @type(Cursor) @default(None)

- The master face. The coupl&#x65;_&#x63;rMasterFace_,_crSlaveFac&#x65;_&#x61;n&#x64;_&#x63;rMPCConnectio&#x6E;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `crSlaveFace` @type(Cursor) @default(None)

- The slave face. The coupl&#x65;_&#x63;rMasterFace_,_crSlaveFac&#x65;_&#x61;n&#x64;_&#x63;rMPCConnectio&#x6E;_&#x61;rguments are mutually exclusive. One of them must be specified.

### `listMpcConnection` @type(List\[MPC\_CONNECTION]) @default(\[])

- The pair of MPC connection data type.

### `iLocalCoordinate` @type(Integer) @default(0)

- The local coordinate system.

### `bUpdateDispCS` @type(Boolean) @default(True)

- Whether or not update displacement coordinate system at nodes belongs to selected faces to the specified local coordinate system.
  - I&#x66;_&#x54;rue_, the displacement coordinate system is updated.
  - I&#x66;_&#x46;alse_, displacement coordinate system is not updated.

### `crMPCConnection` @type(Cursor) @default(None)

- The exist MPC for editing. The coupl&#x65;_&#x63;rMasterFace_,_crSlaveFac&#x65;_&#x61;n&#x64;_&#x63;rMPCConnectio&#x6E;_&#x61;rguments are mutually exclusive. One of them must be specified.
  - If this parameter is used, the specified exist MPC item will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new MPC item will be created.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection (2 Faces).

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.TwoFaces(strName="MPC_12", 
                                               crMasterFace=Face(49),
                                               crSlaveFace=Face(24), 
                                               listMpcConnection=[MPC_CONNECTION(iDof=1), 
                                                                  MPC_CONNECTION(iDof=2),
                                                                  MPC_CONNECTION(iDof=4), 
                                                                  MPC_CONNECTION(), 
                                                                  MPC_CONNECTION(),
                                                                  MPC_CONNECTION()], 
                                               bUpdateDispCS=1)

JPT.Debugger(created_mpc)
```
