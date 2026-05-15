---
title: "MoveNodeAlignNode()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Move Nodes from Node to Element plane

## Syntax

```psj
MoveNodeAlignNode(int[] taRefNodeKeys, int[] taObjNodeKeys, int iType)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Reference node key cursor(Node ID)

<!-- @since:5.0.1 -->
### 2. Int\[]

Object node key cursor(Node ID)

<!-- @since:5.0.1 -->
### 3. Int

Type of searching align node

- 1: On shortest pass
- 2: On the direction the reference nodes
- 3: On selected entity

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MoveNodeAlignNode([150, 140, 148], [141], 2)
```
