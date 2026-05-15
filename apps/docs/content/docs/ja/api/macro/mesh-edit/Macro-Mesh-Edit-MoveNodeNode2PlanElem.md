---
title: "MoveNodeNode2PlanElem()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move Nodes from Node to Element plane

## Syntax

```psj
MoveNodeNode2PlanElem(int[] iNodeKey, int[] iElemkey)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Node key cursor(\[Node ID])

<!-- @since:5.0.1 -->
### 2. Int\[]

Element key cursor(\[Elem ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeNode2PlanElem([187], [883])
```
