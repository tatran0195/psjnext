---
title: "MeshEdit.CreateNode.Offset()"
description: "Create a new node by offsetting a distance from the selected node or floating point"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > Offset"
macro _link: "[CreateNodeOffset](../../macro/mesh-edit/CreateNodeOffset)"
---

## Description

Create a new node by offsetting a distance from the selected node or floating point.

## Syntax

```psj
MeshEdit.CreateNode.Offset(...)
```

## Inputs

<!-- @since:5.0.1 @type:Vector @optional @default:[] -->
<!-- @since:5.1.0 @type:List[Double] -->
### `vecOffset`

- The offset vector.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iRepeat`

- The repeat times.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlNodes`

- The selected nodes to create offset ones.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crCoord`

- The coordinate.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:1 -->
### `iRep`

- The repeat times.

## Return Code

- A _List of Cursor_ specifying the created floating nodes.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create offset node
newNode = MeshEdit.CreateNode.Offset(vecOffset=[0.003, 0.0, 0.0], crlNodes=[Node(7)])
JPT.Debugger(newNode) # for checking the return value
```
