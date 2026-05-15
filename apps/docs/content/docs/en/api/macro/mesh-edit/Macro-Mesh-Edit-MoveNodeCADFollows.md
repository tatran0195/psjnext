---
title: "MoveNodeCADFollows()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move node to mouse drag position

## Syntax

```psj
MoveNodeCADFollows(Cursor[] node, double x, double y, double z)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

List with the nodes to move

<!-- @since:5.0.1 -->
### 2. Double

x: 1st coordinate of the point where to move the node.

<!-- @since:5.0.1 -->
### 3. Double

y: 2nd coordinate of the point where to move the node.

<!-- @since:5.0.1 -->
### 4. Double

z: 3rd coordinate of the point where to move the node.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeCADFollows([10:1992], 0.00523353, 0.01, 0.00789714)
```
