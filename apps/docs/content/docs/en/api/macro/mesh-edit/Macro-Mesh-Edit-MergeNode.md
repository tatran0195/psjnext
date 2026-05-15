---
title: "MergeNode()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Merge Node

## Syntax

```psj
MergeNode(double dTol, int iMergeType, cursor[] vcrTarget, bool createGroup, bool equivalenceNode)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

Tolerance value

<!-- @since:5.0.1 -->
### 2. Int

Merge node type

- 0: First entity
- 1: Second entity
- 2: Highest ID
- 3: Lowest ID

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target entity cursor

<!-- @since:5.0.1 -->
### 4. Bool

Create group bool flag True = 1, False = 0

<!-- @since:5.0.1 -->
### 5. Bool

Equivalence node bool flag True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MergeNode(0.001, 2, [3:1, 10:217, 11:471, 5:28, 6:18], 1, 1)
```
