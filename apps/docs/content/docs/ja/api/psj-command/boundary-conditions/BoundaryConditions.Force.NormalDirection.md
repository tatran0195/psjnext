---
title: "BoundaryConditions.Force.NormalDirection()"
description: "Create a force in the normal direction applies on selected Face, Edge, Node/MidNode, Normal(Element). User inputs the force value, and it will apply the force to the selected items"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Boundary Conditions > Force > Normal Direction"
---

## Description

Create a force in the normal direction applies on selected Face, Edge, Node/MidNode, Normal(Element). User inputs the force value, and it will apply the force to the selected items.

## Syntax

```psj
BoundaryConditions.Force.NormalDirection(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify the name of the force setting.
- The default value is "ForceNormal1".

<!-- @since:5.0.1 @optional -->
### dForce

- Specify the total force value (default unit: N).
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crElemForNormal

- Specify a 2D element. This element will be used to calculate vector normal for force direction.

<!-- @since:5.0.1 @optional -->
### iArrowDir

- Specify the display arrow direction. This parameter only affects the display of the force setting, the force itself remains intact. The value for this parameter is one of the following.
  - 0: Start at node.
  - 1: End at node.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### iDistributeType

- Specify the force distribution method. The value for this parameter is one of the following.
  - 0: Per selected entity. Each selected item (Face, Edge, Node) receives the same amount of the specified force. For example, a vector force \[1; 0; 2] is applied on 2 faces, then each face will receive a vector force \[1; 0; 2].
  - 1: Per selected node. Each nodes in selected items (Face, Edge, Node) receives the same amount of the specified force. For example, a vector force \[1; 0; 2] is applied on 1 edge, which has 10 nodes, then each node will receive a vector force \[1; 0; 2].
  - 2: Total of selected entity. Each selected item (Face, Edge, Node) receives the same amount of force, which is the specified force divided by the number of selected entity. For example, a vector force \[1; 0; 2] is applied on 2 faces, then each face will receive a vector force \[0.5; 0; 1].
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crCoord

- Specify the coordinate from which the fixed constraint is created.
- The default value is _None_(global coordinate system).

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the list of targets for normal direction force. This target can be Face, Edge, Node/MidNode, Normal(Element).
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify an existing normal direction force. If this parameter is used, the specified normal direction force will be modified. If it is left _None_, a new normal direction force will be created.
- The default value is _None_.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube()

created _bcs = BoundaryConditions.Force.NormalDirection(strName="ForceNormal1", 
                                                       dForce=1, 
                                                       crElemForNormal=Elem(1008),
                                                       crlTargets=[Face(26)])

JPT.Debugger(created _bcs)
```
