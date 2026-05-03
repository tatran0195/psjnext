---
title: "Connections.MPC.Equation.MultiNodes()"
description: "Create a MPC connection between a slave node with multi-master nodes"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MPC > Equation > MultiNodes"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create a MPC connection between a slave node with multi-master nodes.

## Syntax

```psj
Connections.MPC.Equation.MultiNodes(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crlMasterNodes` @type(List\[Cursor])

- The list of master nodes which need to be connected. The master nodes are the nodes from the second selected node onwards in the selection list of nodes.
- This is the required input.

### `crSlaveNode` @type(Cursor)

- The slave node which needs to be connected. The slave node is the first selected node in the selection list of nodes. This slave node will connect to all master nodes.
- This is the required input.

### `listMpcConnection` @type(List\[MPC\_CONNECTION]) @default(\[])

- The list of MPC connection.

### `dValue` @type(Double) @default(0.0)

- The MPC value.

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

```psj {6,7,8,9,10,11,12,13,14,15,16,17,18}
Geometry.Part.Cube(iPartColor = 7666683)
Geometry.Part.Cube(dlOrigin = [0.02, 0.0, 0.0], 
                   strName = "Cube_2", 
                   iPartColor = 12867524)

created_mpc = Connections.MPC.Equation.MultipleNodes(crlMasterNodes=[Node(340,
                                                                          344, 
                                                                          353)],
                                                     crSlaveNode=Node(757), 
                                                     listMpcConnection=[MPC_CONNECTION(dCoef=1.0, 
                                                                                       iDof=1),
                                                                        MPC_CONNECTION(dCoef=1.0, 
                                                                                       iDof=1), 
                                                                        MPC_CONNECTION(dCoef=1.0, 
                                                                                       iDof=1),
                                                                        MPC_CONNECTION(dCoef=1.0, 
                                                                                       iDof=1)], 
                                                     bUpdateDispCS=1)

JPT.Debugger(created_mpc)
```
