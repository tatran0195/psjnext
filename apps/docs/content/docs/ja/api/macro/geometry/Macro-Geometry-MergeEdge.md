---
title: "MergeEdge()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Merge Edge

## Syntax

```psj
MergeEdge(cursor[] vcrEdges)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target edges cursor(\[5:Edge ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MergeEdge([5:50, 5:11])
```
