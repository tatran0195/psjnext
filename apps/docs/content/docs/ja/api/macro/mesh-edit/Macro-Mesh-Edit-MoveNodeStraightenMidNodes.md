---
title: "MoveNodeStraightenMidNodes()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move mid-node(s) to correct position

## Syntax

```psj
MoveNodeStraightenMidNodes(int[] taBodyKey, int[] taFaceKey, int[] taEdgeKey, int[] taNodeKey)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Body key cursor(\[Body ID])

<!-- @since:5.0.1 -->
### 2. Int\[]

Face key cursor(\[Face ID])

<!-- @since:5.0.1 -->
### 3. Int\[]

Edge key cursor(\[Edge ID])

<!-- @since:5.0.1 -->
### 4. Int\[]

Node key cursor(\[Node ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeStraightenMidNodes([], [25], [], [444, 460])
```
