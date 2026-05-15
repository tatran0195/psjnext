---
title: "ASMSeparateSolid()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Separate assembled parts in a solid model

## Syntax

```psj
ASMSeparateSolid(int[] bodyID, int[] faceID, bool createGroup)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Int\[]

Given body ids to be separated

<!-- @since:5.0.1 -->
### 2. Int\[]

Given face ids to be assembled

<!-- @since:5.0.1 -->
### 3. Bool

Group creation option

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ASMSeparateSolid([2, 29], [], 0)
```
