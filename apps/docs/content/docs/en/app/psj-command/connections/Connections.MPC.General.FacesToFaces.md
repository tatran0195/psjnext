---
title: "Connections.MPC.General.FacesToFaces()"
description: "Create MPC by connecting selected faces together"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MPC > General > FacesToFaces"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC by connecting selected faces together.

## Syntax

```psj
Connections.MPC.General.FacesToFaces(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crlMasterFaces` @type(List\[Cursor])

- The list of the master faces which need to be connected. The master list can contain one or many faces.
- In case the master list has more than one face, the number of master faces and slave faces must be equal. The MPC is created by connecting the selected master faces with the selected slave faces one by one correspondingly.
- This is the required input.

### `crlSlaveFaces` @type(List\[Cursor])

- The list of the slave faces which need to be connected. The slave list can contain one or many faces.
- In case the slave list has more than one face, the number of slave faces and master faces must be equal. The MPC is created by connecting the selected master faces with the selected slave faces one by one correspondingly.
- This is the required input.

### `listMpcConnection` @type(List\[MPC\_CONNECTION]) @default(\[])

- The list of MPC connection.

### `iLocalCoordinate` @type(Integer) @default(0)

- The local coordinate system.

### `bUpdateDispCS` @type(Boolean) @default(True)

- The update displacement coordinate system.
  - I&#x66;_&#x54;rue_, the displacement coordinate system is updated.
  - I&#x66;_&#x46;alse_, displacement coordinate system is not updated.

### `crMPCConnection` @type(Cursor) @default(None)

- An existing MPC connection.
  - If this parameter is used, the specified MPC connection will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new MPC connection will be created.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.FacesToFaces(strName="MPC_10", 
                                                   crlMasterFaces=[Face(24)],
                                                   crlSlaveFaces=[Face(49)], 
                                                   listMpcConnection=[MPC_CONNECTION(iDof=1), 
                                                                      MPC_CONNECTION(iDof=2),
                                                                      MPC_CONNECTION(iDof=4), 
                                                                      MPC_CONNECTION(), 
                                                                      MPC_CONNECTION(), 
                                                                      MPC_CONNECTION()], 
                                                   bUpdateDispCS=1, 
                                                   crMPCConnection=None)

JPT.Debugger(created_mpc)
```
