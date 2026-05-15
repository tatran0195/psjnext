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

<!-- @since:5.0.1 @required -->
### crStartNode

- Specify the start node.

<!-- @since:5.0.1 @required -->
### crEndNode

- Specify the end node.

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of new part.
- The default value is "Bar\_1".

<!-- @since:5.0.1 @optional -->
### iMeshOption

- Specify the option to generate element on Bar body.
  - If _iMeshOption=0_: The new Bar body has the number of 1D elements equal to _iMeshCount_.
  - If _iMeshOption=1_: The new Bar body has the size of 1D elements on the Bar body equal to _dMeshSize_.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iMeshCount

- Specify the number of 1D elements on the Bar body. This argument should be specified when _iMeshOption=0_.
- The default value is 5.

<!-- @since:5.0.1 @optional -->
### dMeshSize

- Specify the size of 1D elements on the Bar body. This argument should be specified when _iMeshOption=1_.
- The default value is 0.0.

## Return Code

A _Cursor_ specifying the created bar part.

## Sample Code

```psj {3}
Geometry.Part.Cube()

newBar = Geometry.Bar.TwoNodes(crStartNode=Node(5), crEndNode=Node(7))
JPT.Debugger(newBar)
```
