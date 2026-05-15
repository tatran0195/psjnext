---
title: "SeparateNode()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Separate Node

## Syntax

```psj
SeparateNode(cursor[] vcrNode, cursor[] vcrTarget, int iKeepIDsOn)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target node cursor(\[10:Node ID])

<!-- @since:5.0.1 -->
### 2. Cursor\[]

Target entities cursor

<!-- @since:5.0.1 -->
### 3. Int

Keep Node IDs On type

- 0: None
- 1: Selection Part Order
- 2: Higher Part ID
- 3: Lower Part ID

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SeparateNode([10:7, 10:1955, 10:1954, 10:1953], [10:7, 10:1955, 10:1954, 10:1953], 0)
```
