---
title: "Connections.RigidElements.RBE2.OneToOne()"
description: "Create one-to-one (master:slave) RBE2 (rigid element)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBE2 > OneToOne"
macro _link: "[RBE2OneToOne](../../macro/connections/RBE2OneToOne)"
---

## Description

Create one-to-one (master:slave) RBE2 (rigid element).

## Syntax

```psj
Connections.RigidElements.RBE2.OneToOne(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:17 -->
### `iMethod`

- The connection method.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The master target. Master target can be selected by part, face, edge, element, or node.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The slave target. Slave target can be selected by part, face, edge, element, or node.

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

- The surface definition.
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

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iEnableCheckDulplicate`

- The enable check dulplicate.

## Return Code

A _Cursor_ specifying the created RBE2.

## Sample Code

```psj {6,7}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=7463537)

# Create the connections
rbe2 _connection = Connections.RigidElements.RBE2.OneToOne(crlMasterTargets=[Node(496)], 
                                            crlSlaveTargets=[Node(7)], strName="RBE2 _3")
JPT.Debugger(rbe2 _connection)
```
