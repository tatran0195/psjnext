---
title: "Connections.MPC.General.TwoNodes()"
description: "Create a MPC connection between slave nodes to master nodes one-to-one correspondingly. The sequence of nodes selection is the first master node, the first slave node, the second master node, the second slave node and so on"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Connections > MPC > General > NodeToNode"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create a MPC connection between slave nodes to master nodes one-to-one correspondingly. The sequence of nodes selection is the first master node, the first slave node, the second master node, the second slave node and so on.

## Syntax

```psj
Connections.MPC.General.TwoNodes(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crlMasterNodes` @type(List\[Cursor])

- The list of master nodes which need to be connected. The master list can contain one or many nodes.
- In case the list has more than one node, the number of master nodes and slave nodes must be equal. The MPC is created by connecting the selected master nodes with the selected slave nodes one by one correspondingly.
- This is the required input.

### `crlSlaveNodes` @type(List\[Cursor])

- The list of slave nodes which need to be connected. The slave list can contain one or many nodes.
- In case the list has more than one face, the number of master nodes and slave nodes must be equal. The MPC is created by connecting the selected master nodes with the selected slave nodes one by one correspondingly.
- This is the required input.

### `listMpcConnection` @type(List\[MPC\_CONNECTION]) @default(\[])

- The list of MPC connection.

### `iLocalCoordinate` @type(Integer) @default(0)

- The local coordinate system.

### `bUpdateDispCS` @type(Boolean) @default(True)

- Whether or not update displacement coordinate system.
  - I&#x66;_&#x54;rue_, the displacement coordinate system is updated.
  - I&#x66;_&#x46;alse_, displacement coordinate system is not updated.

### `crMPCConnection` @type(Cursor) @default(None)

- An existing MPC connection.
  - If this parameter is used, the specified MPC connection will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new MPC connection will be created.

## Return Code

A _Cursor_ specifying the created or the modified MPC connection.

## Sample Code

```psj {6-15}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.TwoNodes(strName="MPC_10", 
                                               crlMasterNodes=[Node(757)],
                                               crlSlaveNodes=[Node(347)], 
                                               listMpcConnection=[MPC_CONNECTION(iDof=1), 
                                                                  MPC_CONNECTION(iDof=2),
                                                                  MPC_CONNECTION(iDof=4), 
                                                                  MPC_CONNECTION(), 
                                                                  MPC_CONNECTION(), 
                                                                  MPC_CONNECTION()],
                                               bUpdateDispCS=1)

JPT.Debugger(created_mpc)
```
