---
title: "Collapse()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Collapse Element Edge

## Syntax

```psj
Collapse(cursor crNodeRef, cursor crNodeEq)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor

Node for reference (10:Node ID)

<!-- @since:5.0.1 -->
### 2. Cursor

Node for equivalence (10:Node ID)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Collapse(10:489, 10:490)
```
