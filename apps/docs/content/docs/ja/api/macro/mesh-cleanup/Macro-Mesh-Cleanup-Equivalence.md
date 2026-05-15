---
title: "Equivalence()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Equivalence Nodes

## Syntax

```psj
Equivalence(cursor[] taNode, int iTypeEquiva, double tolerance)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target node cursor(\[10:Node ID])

<!-- @since:5.0.1 -->
### 2. Int

Equivalence merge toward type

- 0: First Node
- 1: Second Node
- 2: Mid-Node

<!-- @since:5.0.1 -->
### 3. Double

Equivalence tolerance

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Equivalence([10:489, 10:84], 0, 0.001)
```
