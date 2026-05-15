---
title: "MergeFace _MergeEntities()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Merge Face

## Syntax

```psj
MergeFace _MergeEntities(cursor[] taFace, bool bMergeEdge)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target faces cursor(\[6:Face ID])

<!-- @since:5.0.1 -->
### 2. Bool

Whether merge edges or not True = 1, False = 0

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MergeFace _MergeEntities([6:22, 6:47], 1)
```
