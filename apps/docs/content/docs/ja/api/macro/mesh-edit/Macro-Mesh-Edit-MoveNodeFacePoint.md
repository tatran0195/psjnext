---
title: "MoveNodeFacePoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move node(s) to a Face Point position

## Syntax

```psj
MoveNodeFacePoint(double x, double y, double z, int[] node _list)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

x: 1st coordinate of the point where to move the node.

<!-- @since:5.0.1 -->
### 2. Double

y: 2nd coordinate of the point where to move the node.

<!-- @since:5.0.1 -->
### 3. Double

z: 3rd coordinate of the point where to move the node.

<!-- @since:5.0.1 -->
### 4. Int\[]

List with the nodes to move

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeFacePoint(0.00505433,0.01,0.00508144, [191, 215])
```
