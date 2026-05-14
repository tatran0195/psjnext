---
title: "Connections.RigidElements.RBE2.OneToOneNodesWithTolerance()"
description: "Create one-to-one (master:slave) RBE2 (rigid elements) with nodes tolerance"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE2 > OneToOneNodesWithTolerance"
macro _link: "[RBE2OneToOneNodesWithTolerance](../../macro/connections/RBE2OneToOneNodesWithTolerance)"
---

## Description

Create one-to-one (master:slave) RBE2 (rigid elements) with nodes tolerance.

## Syntax

```psj
Connections.RigidElements.RBE2.OneToOneNodesWithTolerance(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:21 -->
### `iMethod`

- The connection method.

<!-- ### `crlMasterTargets`

- A _List of Cursor_ specifying the master target. Master target can be selected by node only.
- The default value is [].

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target. Slave target can be selected by node only.
- The default value is []. -->

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target nodes.

<!-- @since:5.0.1 @type:Integer @optional @default:2 -->
### `iEType`

- The connection type.

<!-- @since:5.0.1 @type:String @optional @default:"RBE2 _1" -->
### `strName`

- The RBE2 name to be created.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoordSys`

- The coordinate system.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dTolerance`

- The tolerance.

<!-- @since:5.0.1 @type:Integer @optional @default:63 -->
### `iUlDOFs`

- The component of dependent degrees of freedom.

<!-- @since:5.0.1 @type:Double List @optional @default:[0, 0, 0] -->
<!-- @since:5.1.0 @type:List[Double] -->
### `dlVirtualNodePos`

- The virtual node position.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iSurfaceDef`

- The surface definition output.
  - 0: By Node Set - Specify the node as a reference surface.
  - 1: By Element Set - Specify the element as a reference surface. Cannot configure an element to the slave entity (node, edge) and if it has been selected an error will be output.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing RBE2 connection
  - If this parameter is used, the specified RBE2 connection will be modified.
  - If it is left None, a new RBE2 will be created.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEnableUpdateDispCS`

- Whether to update displacement coordinate system.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iEnableCornerOnly`

- Whether to connect only to the corner nodes of the selected entity.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iEnableCheckDuplicate`

- Whether to check for duplicate.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iDuplicateMode`

- The duplicate mode.

<!-- @since:5.0.1 @type:List[Cursor] @removed:5.1.0 @optional @deprecated @default:[] -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @removed:5.1.0 @optional @deprecated @default:[] -->
### `crlSlaveTargets`

- The slave target.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iEnableCheckDulplicate`

- The enable check dulplicate.

## Return Code

A _Cursor_ specifying the created RBE2.

## Sample Code

```psj {6-9}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], strName="Cube _2", iPartColor=7463537)

# Create the connections
rbe2 _connection = Connections.RigidElements.RBE2.OneToOneNodesWithTolerance(crlTargets =[Node(493, 6, 496, 7)], 
                                                                            strName="RBE2 _1", 
                                                                            dTolerance=0.005, 
                                                                            iUlDOFs=7)
JPT.Debugger(rbe2 _connection)
```
