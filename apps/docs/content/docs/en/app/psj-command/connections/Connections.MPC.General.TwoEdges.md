---
title: "Connections.MPC.General.TwoEdges()"
description: "Create MPC between two edges"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > MPC > General > TwoEdges"
macro_link: "[Mpc](../../macro/connections/Mpc)"
---

## Description

Create MPC between two edges.

## Syntax

```psj
Connections.MPC.General.TwoEdges(...)
```

## Inputs

### `strName` @type(String) @default("MPC\_1")

- The MPC name.

### `crMasterEdge` @type(List\[Cursor])

- The list of master edges which need to be connected.
- This is the required input.

### `crSlaveEdge` @type(List\[Cursor])

- The list of slave edges which need to be connected.
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

```psj {6,7,8,9,10,11,12,13,14,15}
Geometry.Part.Cube(iPartColor=7666683)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], 
                   strName="Cube_2", 
                   iPartColor=12867524)

created_mpc = Connections.MPC.General.TwoEdges(strName="MPC_11", 
                                               crMasterEdge=Edge(46),
                                               crSlaveEdge=Edge(10), 
                                               listMpcConnection=[MPC_CONNECTION(iDof=1), 
                                                                  MPC_CONNECTION(iDof=2),
                                                                  MPC_CONNECTION(iDof=4), 
                                                                  MPC_CONNECTION(iDof=8), 
                                                                  MPC_CONNECTION(),
                                                                  MPC_CONNECTION(iDof=32)], 
                                               bUpdateDispCS=1)

JPT.Debugger(created_mpc)
```
