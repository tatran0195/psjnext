---
title: "MoveNodeNormalOffset()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move node(s) in Normal Direction of plane

## Syntax

```psj
MoveNodeNormalOffset(double posMagnitude, int[] iNodeKey)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

Position magnitude

<!-- @since:5.0.1 -->
### 2. Int\[]

Node key cursor(\[Node ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeNormalOffset(0.002, [1432])
```
