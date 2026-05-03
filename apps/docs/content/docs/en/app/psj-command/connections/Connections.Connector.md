---
title: "Connections.Connector()"
description: "Create connectors between nodes, edges, and faces according to specified connection types. User selects master/slave targets and the connectors will be created to connect nodes on master/slave targets with each other"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Connector"
macro_link: "[Connector](../../macro/connections/Connector)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Create connectors between nodes, edges, and faces according to specified connection types. User selects master/slave targets and the connectors will be created to connect nodes on master/slave targets with each other.

## Syntax

```psj
Connections.Connector(...)
```

## Inputs

### `strName` @type(String) @default("Connector\_1")

- The connection name to be created.

### `iMethod` @type(Integer) @default(1)

- The connection method.
  - I&#x66;_&#x69;Method=1_, the method is Node to Node.
  - I&#x66;_&#x69;Method=2_, the method is Edge to Edge.
  - I&#x66;_&#x69;Method=3_, the method is Face to Face.

### `iConnectType` @type(Integer) @default(0)

- The connection type.
  - I&#x66;_&#x69;ConnectType=0_, the connection type is Parallel.
  - I&#x66;_&#x69;ConnectType=1_, the connection type is Translation.
  - I&#x66;_&#x69;ConnectType=2_, the connection type is Rotation.
  - I&#x66;_&#x69;ConnectType=3_, the connection type is Bushing.
  - I&#x66;_&#x69;ConnectType=4_, the connection type is Cylindrical.
  - I&#x66;_&#x69;ConnectType=5_, the connection type is Joint.
  - I&#x66;_&#x69;ConnectType=6_, the connection type is RigidRod.
  - I&#x66;_&#x69;ConnectType=7_, the connection type is RigidBar.

### `iRefNode` @type(Integer) @default(0)

- A node to refer to when determining the coordinate system.
  - I&#x66;_&#x69;RefNode=0_, reference to the first node.
  - I&#x66;_&#x69;RefNode=1_, reference to the second node.

### `iElemCs` @type(Integer) @default(0)

- The option whether or not an element coordinate system is used.
  - I&#x66;_&#x69;ElemCs=0_, do not use element coordinate system.
  - I&#x66;_&#x69;ElemCs=1_, use element coordinate system.

### `crLocalCS` @type(Cursor) @default(None)

- The local coordinate system.

### `crlElasticity` @type(List\[Cursor]) @default(\[])

- The table data of elastic property.

### `crlDamp` @type(List\[Cursor]) @default(\[])

- The table data of viscosity characteristics.

### `crlMasterTargets` @type(List\[Cursor]) @default(\[])

- The list of master targets.
  - The targets are nodes when th&#x65;_&#x69;Metho&#x64;_&#x69;s equal to 1.
  - The targets are edges when th&#x65;_&#x69;Metho&#x64;_&#x69;s equal to 2.
  - And the targets are faces when th&#x65;_&#x69;Metho&#x64;_&#x69;s equal to 3.

### `crlSlaveTargets` @type(List\[Cursor]) @default(\[])

- The list of slave targets.
  - The targets are nodes when th&#x65;_&#x69;Metho&#x64;_&#x69;s equal to 1.
  - The targets are edges when th&#x65;_&#x69;Metho&#x64;_&#x69;s equal to 2.
  - And the targets are faces when th&#x65;_&#x69;Metho&#x64;_&#x69;s equal to 3.

### `crEdit` @type(Cursor) @default(None)

- An existing connection.
  - If this parameter is used, the specified connection will be modified.
  - If it is lef&#x74;_&#x4E;one_, a new connection will be created.

### `iEffectiveDofs` @type(Integer) @default(0) @since(5.1.0)

- The effective degrees of freedom as a bitmask.
  - I&#x66;_&#x69;EffectiveDofs=1_, the DOF is Tx (Translation X).
  - I&#x66;_&#x69;EffectiveDofs=2_, the DOF is Ty (Translation Y).
  - I&#x66;_&#x69;EffectiveDofs=4_, the DOF is Tz (Translation Z).
  - I&#x66;_&#x69;EffectiveDofs=8_, the DOF is Rx (Rotation X).
  - I&#x66;_&#x69;EffectiveDofs=16_, the DOF is Ry (Rotation Y).
  - I&#x66;_&#x69;EffectiveDofs=32_, the DOF is Rz (Rotation Z).
  - Example: To enable Tx + Rx + Ry →`1 + 8 + 16 = 25`.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {3-18}
Geometry.Part.Cube()

created_contact = Connections.Connector(strName="Connector_1", 
                                        iMethod=3, 
                                        crlElasticity=[Unknown(0, 
                                                               0, 
                                                               0, 
                                                               0,
                                                               0, 
                                                               0)], 
                                        crlDamp=[Unknown(0, 
                                                         0, 
                                                         0, 
                                                         0, 
                                                         0, 
                                                         0)], 
                                        crlMasterTargets=[Face(22)], 
                                        crlSlaveTargets=[Face(21)])

JPT.Debugger(created_contact)
```
