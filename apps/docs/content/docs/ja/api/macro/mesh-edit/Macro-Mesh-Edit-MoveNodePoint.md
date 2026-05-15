---
title: "MoveNodePoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move node(s) to an Face(Edge) Point position

## Syntax

```psj
MoveNodePoint(double dDeltaX, double dDeltaY, double dDeltaZ, int[] taNodeKey)
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
### 4. Int\[]

Node key cursor(\[Node ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodePoint(0.0044675, 0.0056845, -3.46945e-18, [410, 369])
```
