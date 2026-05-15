---
title: "MoveNodeOffset()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move node(s) to an offset position

## Syntax

```psj
MoveNodeOffset(double dDeltaX, double dDeltaY, double dDeltaZ, cursor crCoord, int[] taNodeKey)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

X coordinate to move the node

<!-- @since:5.0.1 -->
### 2. Double

Y coordinate to move the node

<!-- @since:5.0.1 -->
### 3. Double

Z coordinate to move the node

<!-- @since:5.0.1 -->
### 4. Cursor

Whether use local coordinate or not True = 27:\*, False = 0:0

<!-- @since:5.0.1 -->
### 5. Int\[]

Node key cursor(\[Node ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeOffset(0, 0, 0.0005, 0:0, [1068])
```
