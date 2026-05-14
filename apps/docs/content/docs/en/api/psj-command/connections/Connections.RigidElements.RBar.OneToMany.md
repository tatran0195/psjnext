---
title: "Connections.RigidElements.RBar.OneToMany()"
description: "Create one-to-many (master:slave) RBar (rigid elements)"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBar > OneToMany"
macro _link: "[RBarOneToMany](../../macro/connections/RBarOneToMany)"
---

## Description

Create one-to-many (master:slave) RBar (rigid elements).

## Syntax

```psj
Connections.RigidElements.RBar.OneToMany(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"RBAR _1" -->
### `strName`

- The RBar name to be created.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlMasterTargets`

- The master target. Master target can be selected by part, face, edge, element, or node.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlSlaveTargets`

- The slave target. Slave target can be selected by part, face, edge, element, or node.

<!-- @since:5.0.1 @type:Integer @optional @default:16 -->
### `iMethod`

- The connection method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iUlDOFs`

- The master degrees of freedom. This function only support case where all components of the independent degrees of freedom are fixed for the nodes selected in the master.

<!-- @since:5.0.1 @type:Double @optional @default:DFLT _DBL -->
### `dTol`

- The tolerance.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate system.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bUpdateDispCS`

- Whether or not update displacement coordinate system.
  - If True, the displacement coordinate system is updated.
  - If False, displacement coordinate system is not updated.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Rbar
  - If this parameter is used, the specified Rbar will be modified.
  - If it is left None, a new RBar will be created.

## Return Code

A _Cursor_ specifying the created Rbar.

## Sample Code

```psj {6,7}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube _2", iPartColor=7463537)

# Create the connections
rbar _connection = Connections.RigidElements.RBar.OneToMany(strName="RBar _1", crlMasterTargets=[Node(496)], 
                                crlSlaveTargets=[Node(7, 85, 6)], iUlDOFs=63, dTol=0.0, bUpdateDispCS=True)
JPT.Debugger(rbar _connection)
```
