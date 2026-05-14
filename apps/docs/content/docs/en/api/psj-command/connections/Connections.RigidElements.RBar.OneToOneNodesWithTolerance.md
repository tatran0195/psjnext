---
title: "Connections.RigidElements.RBar.OneToOneNodesWithTolerance()"
description: "Create one-to-one (master:slave) RBar (rigid elements) with nodes tolerance"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > RigidElements > RBar > OneToOneNodesWithTolerance"
macro _link: "[RBarOneToOneNodesWithTolerance](../../macro/connections/RBarOneToOneNodesWithTolerance)"
---

## Description

Create one-to-one (master:slave) RBar (rigid elements) with nodes tolerance.

## Syntax

```psj
Connections.RigidElements.RBar.OneToOneNodesWithTolerance(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"RBAR _1" -->
### `strName`

- The RBar name to be created.

<!-- ### `crlMasterTargets`

- A _List of Cursor_ specifying the master target. Master target can be selected by node only.
- The default value is [].

### `crlSlaveTargets`

- A _List of Cursor_ specifying the slave target. Slave target can be selected by node only.
- The default value is []. -->

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target nodes.

<!-- @since:5.0.1 @type:Integer @optional @default:21 -->
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
  - If it is left None, a new Rbar will be created.

<!-- @since:5.0.1 @type:List[Cursor] @removed:5.1.0 @optional @deprecated @default:[] -->
### `crlMasterTargets`

- The master target.

<!-- @since:5.0.1 @type:List[Cursor] @removed:5.1.0 @optional @deprecated @default:[] -->
### `crlSlaveTargets`

- The slave target.

## Return Code

A _Cursor_ specifying the created Rbar.

## Sample Code

```psj {6-9}
# Prepare models
Geometry.Part.Cube(iPartColor=6409934)
Geometry.Part.Cube(dlOrigin=[0.015, 0.0, 0.0], strName="Cube _2", iPartColor=7463537)

# Create the connections
rbar _connection = Connections.RigidElements.RBar.OneToOneNodesWithTolerance(strName="RBar _1", 
                                                                            crlTargets =[Node(493, 6, 496, 7)], 
                                                                            iUlDOFs=63, 
                                                                            dTol=0.005)
JPT.Debugger(rbar _connection)
```
