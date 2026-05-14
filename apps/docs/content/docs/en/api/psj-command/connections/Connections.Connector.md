---
title: "Connections.Connector()"
description: "Create connectors between nodes, edges, and faces according to specified connection types. User selects master/slave targets and the connectors will be created to connect nodes on master/slave targets with each other"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Connector"
macro _link: "[Connector](../../macro/connections/Connector)"
---

## Description

Create connectors between nodes, edges, and faces according to specified connection types. User selects master/slave targets and the connectors will be created to connect nodes on master/slave targets with each other.

## Syntax

```psj
Connections.Connector(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"Connector _1" -->
### `strName`

- The connection name to be created.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iMethod`

- The connection method.
  - If _iMethod=1_, the method is Node to Node.
  - If _iMethod=2_, the method is Edge to Edge.
  - If _iMethod=3_, the method is Face to Face.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iConnectType`

- The connection type.
  - If _iConnectType=0_, the connection type is Parallel.
  - If _iConnectType=1_, the connection type is Translation.
  - If _iConnectType=2_, the connection type is Rotation.
  - If _iConnectType=3_, the connection type is Bushing.
  - If _iConnectType=4_, the connection type is Cylindrical.
  - If _iConnectType=5_, the connection type is Joint.
  - If _iConnectType=6_, the connection type is RigidRod.
  - If _iConnectType=7_, the connection type is RigidBar.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRefNode`

- A node to refer to when determining the coordinate system.
  - If _iRefNode=0_, reference to the first node.
  - If _iRefNode=1_, reference to the second node.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iElemCs`

- The option whether or not an element coordinate system is used.
  - If _iElemCs=0_, do not use element coordinate system.
  - If _iElemCs=1_, use element coordinate system.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crLocalCS`

- The local coordinate system.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlElasticity`

- The table data of elastic property.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlDamp`

- The table data of viscosity characteristics.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The list of master targets.
  - The targets are nodes when the _iMethod_ is equal to 1.
  - The targets are edges when the _iMethod_ is equal to 2.
  - And the targets are faces when the _iMethod_ is equal to 3.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The list of slave targets.
  - The targets are nodes when the _iMethod_ is equal to 1.
  - The targets are edges when the _iMethod_ is equal to 2.
  - And the targets are faces when the _iMethod_ is equal to 3.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing connection.
  - If this parameter is used, the specified connection will be modified.
  - If it is left _None_, a new connection will be created.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iEffectiveDofs`

- The effective degrees of freedom as a bitmask.
  - If _iEffectiveDofs=1_, the DOF is Tx (Translation X).
  - If _iEffectiveDofs=2_, the DOF is Ty (Translation Y).
  - If _iEffectiveDofs=4_, the DOF is Tz (Translation Z).
  - If _iEffectiveDofs=8_, the DOF is Rx (Rotation X).
  - If _iEffectiveDofs=16_, the DOF is Ry (Rotation Y).
  - If _iEffectiveDofs=32_, the DOF is Rz (Rotation Z).
  - Example: To enable Tx + Rx + Ry → `1 + 8 + 16 = 25`.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {3-18}
Geometry.Part.Cube()

created _contact = Connections.Connector(strName="Connector _1", 
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

JPT.Debugger(created _contact)
```
