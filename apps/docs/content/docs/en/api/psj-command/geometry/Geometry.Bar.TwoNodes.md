---
title: "Geometry.Bar.TwoNodes()"
description: "Create a Bar part from two selected nodes"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Geometry > Bar > 2 Nodes"
macro _link: "[CreateBar](../../macro/geometry/CreateBar)"
---

## Description

Create a Bar part from two selected nodes.

## Syntax

```psj
Geometry.Bar.TwoNodes(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crStartNode`

- The start node.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crEndNode`

- The end node.

<!-- @since:5.0.1 @type:String @optional @default:"Bar _1" -->
### `strName`

- The name of new part.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iMeshOption`

- The option to generate element on Bar body.
  - If _iMeshOption=0_: The new Bar body has the number of 1D elements equal to _iMeshCount_.
  - If _iMeshOption=1_: The new Bar body has the size of 1D elements on the Bar body equal to _dMeshSize_.

<!-- @since:5.0.1 @type:Integer @optional @default:5 -->
### `iMeshCount`

- The number of 1D elements on the Bar body. This argument should be specified when _iMeshOption=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0.0 -->
### `dMeshSize`

- The size of 1D elements on the Bar body. This argument should be specified when _iMeshOption=1_.

## Return Code

A _Cursor_ specifying the created bar part.

## Sample Code

```psj {3}
Geometry.Part.Cube()

newBar = Geometry.Bar.TwoNodes(crStartNode=Node(5), crEndNode=Node(7))
JPT.Debugger(newBar)
```
