---
title: "MeshEdit.CreateNode.CenterOfGravity()"
description: "create node Center Of Gravity"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "MeshEdit > CreateNode > CenterOfGravity"
---

## Description

Create node Center Of Gravity

## Syntax

```psj
MeshEdit.CreateNode.CenterOfGravity(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iCreationType`

- The creation type.
  - 0: Gravity
  - 1: Shape

<!-- @since:5.1.0 @type:Integer @optional @default:the maximum node ID + 1 -->
### `iNewNodeID`

- The new node ID.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlParts`

- The selected part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlBarPart`

- The selected bar part.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlFaces`

- The selected face.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @optional @deprecated @default:0 -->
### `iNodeID`

- The node ID.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dX`

- The x.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dY`

- The y.

<!-- @since:5.0.1 @type:Double @removed:5.1.0 @optional @deprecated @default:0.0 -->
### `dZ`

- The z.

## Return Code

- A _Cursor_ specifying the created floating node.

## Sample Code

```psj {5}
# Prepare model
Geometry.Part.Cube()

# Create center node of gravity
newNode = MeshEdit.CreateNode.CenterOfGravity(iNodeID=489, crlTargets=[Part(1)])
JPT.Debugger(newNode) # for checking the return value
```
