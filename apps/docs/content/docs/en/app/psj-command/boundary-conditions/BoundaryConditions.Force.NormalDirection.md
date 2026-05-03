---
title: "BoundaryConditions.Force.NormalDirection()"
description: "Create a force in the normal direction applies on selected Face, Edge, Node/MidNode, Normal(Element). User inputs the force value, and it will apply the force to the selected items"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Boundary Conditions > Force > Normal Direction"
---

## Description

Create a force in the normal direction applies on selected Face, Edge, Node/MidNode, Normal(Element). User inputs the force value, and it will apply the force to the selected items.

## Syntax

```psj
BoundaryConditions.Force.NormalDirection(...)
```

## Inputs

### `strName` @type(String) @default("ForceNormal1")

- The name of the force setting.

### `dForce` @type(Double) @default(0)

- The total force value (default unit: N).

### `crElemForNormal` @type(Cursor)

- A 2D element. This element will be used to calculate vector normal for force direction.

### `iArrowDir` @type(Integer) @default(0)

- The display arrow direction. This parameter only affects the display of the force setting, the force itself remains intact. The value for this parameter is one of the following.
  - 0: Start at node.
  - 1: End at node.

### `iDistributeType` @type(Integer) @default(0)

- The force distribution method. The value for this parameter is one of the following.
  - 0: Per selected entity. Each selected item (Face, Edge, Node) receives the same amount of the specified force. For example, a vector force \[1; 0; 2] is applied on 2 faces, then each face will receive a vector force \[1; 0; 2].
  - 1: Per selected node. Each nodes in selected items (Face, Edge, Node) receives the same amount of the specified force. For example, a vector force \[1; 0; 2] is applied on 1 edge, which has 10 nodes, then each node will receive a vector force \[1; 0; 2].
  - 2: Total of selected entity. Each selected item (Face, Edge, Node) receives the same amount of force, which is the specified force divided by the number of selected entity. For example, a vector force \[1; 0; 2] is applied on 2 faces, then each face will receive a vector force \[0.5; 0; 1].

### `crCoord` @type(Cursor) @default(None(global coordinate system))

- The coordinate from which the fixed constraint is created.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The list of targets for normal direction force. This target can be Face, Edge, Node/MidNode, Normal(Element).

### `crEdit` @type(Cursor) @default(None)

- An existing normal direction force. If this parameter is used, the specified normal direction force will be modified. If it is lef&#x74;_&#x4E;one_, a new normal direction force will be created.

## Return Code

A _Cursor_ specifying the created LBC.

## Sample Code

```psj {3,4,5,6}
Geometry.Part.Cube()

created_bcs = BoundaryConditions.Force.NormalDirection(strName="ForceNormal1", 
                                                       dForce=1, 
                                                       crElemForNormal=Elem(1008),
                                                       crlTargets=[Face(26)])

JPT.Debugger(created_bcs)
```
