---
title: "Connections.MPC.General.NodeToAny()"
description: "Create MPC between a selected node and any types of entities such as nodes, edges or faces"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MPC > General > NodeToAny"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between a selected node and any types of entities such as nodes, edges or faces.

## Syntax

```psj
Connections.MPC.General.NodeToAny(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crMasterNode` @type(Cursor) @default(None)

- The master node which needs to be connected.

### `crlSlaveEntities` @type(List\[Cursor])

- The list of slave entities such as nodes, edges or faces which need to be connected. The slave entities list can contain different types of entities at the same time.
- This is the required input.

### `listMpcConnection` @type(List\[MPC\_CONNECTION]) @default(\[])

- The pair of MPC connection data type.

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

```psj {6,7,8,9,10,11,12,13,14,15,16}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.NodeToAny(strName="MPC_7", 
                                                crMasterNode=Node(757),
                                                crlSlaveEntities=[Node(333), 
                                                                  Edge(14)], 
                                                listMpcConnection=[MPC_CONNECTION(iDof=1),
                                                                   MPC_CONNECTION(iDof=2), 
                                                                   MPC_CONNECTION(iDof=4), 
                                                                   MPC_CONNECTION(), 
                                                                   MPC_CONNECTION(),
                                                                   MPC_CONNECTION()], 
                                                bUpdateDispCS=1)
    
JPT.Debugger(created_mpc)
```
