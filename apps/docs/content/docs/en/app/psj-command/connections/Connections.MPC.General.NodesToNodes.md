---
title: "Connections.MPC.General.NodesToNodes()"
description: "Create MPC between selected nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MPC > General > NodesToNodes"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between selected nodes.

## Syntax

```psj
Connections.MPC.General.NodesToNodes(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crlMasterNodes` @type(List\[Cursor])

- The list of master nodes.
- In case this list has more than one selected node, the number of master nodes and slave nodes must be equal. The MPC is created by connecting selected master nodes with selected slave nodes one-to-one correspondingly.
- This is the required input.

### `crlSlaveNodes` @type(List\[Cursor])

- The list of slave nodes.
- In case this list has more than one selected node, the number of slave nodes and master nodes must be equal. The MPC is created by connecting selected master nodes with selected slave nodes correspondingly.
- This is the required input.

### `listMpcConnection` @type(List\[MPC\_CONNECTION]) @default(\[])

- The pair of MPC connection data type.

### `dSearchTol` @type(Double) @default(0.0)

- The MPC search tolerance value.

### `dValue` @type(Double) @default(0.0)

- The MPC value.

### `iMPCType` @type(Integer) @default(0)

- The MPC type.
  - 0: MPC General.
  - 1: MPC Equation.

### `iSearchType` @type(Integer) @default(1)

- The search type.

### `iLocalCoordinate` @type(Integer) @default(0)

- The local coordinate system.

### `bUpdateDispCS` @type(Boolean) @default(True)

- Whether or not update displacement coordinate system.
  - I&#x66;_&#x54;rue_, the displacement coordinate system is updated.
  - I&#x66;_&#x46;alse_, displacement coordinate system is not updated.

### `crMPCConnection` @type(Cursor) @default(None)

- The exist MPC for editing.
  - If this parameter is used, the specified exist MPC item will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new MPC item will be created.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection.

## Sample Code

```psj {6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.NodesToNodes(strName="MPC_5", 
                                                   crlMasterNodes=[Node(760, 
                                                                        770)],
                                                   crlSlaveNodes=[Node(323, 
                                                                       310)], 
                                                   listMpcConnection=[MPC_CONNECTION(dCoef=1.0, 
                                                                                     iDof=1),
                                                                      MPC_CONNECTION(dCoef=1.0, 
                                                                                     iDof=2), 
                                                                      MPC_CONNECTION(dCoef=1.0, 
                                                                                     iDof=4), 
                                                                      MPC_CONNECTION(),
                                                                      MPC_CONNECTION(), 
                                                                      MPC_CONNECTION()], 
                                                   bUpdateDispCS=1)
    
JPT.Debugger(created_mpc)
```
