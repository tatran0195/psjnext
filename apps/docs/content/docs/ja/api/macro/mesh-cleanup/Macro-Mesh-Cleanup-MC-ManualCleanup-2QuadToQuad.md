---
title: "MC _ManualCleanup _2QuadToQuad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Merge two Quad elements into one Quad element

## Syntax

```psj
MC _ManualCleanup _2QuadtoQuad(cursor[] elemList)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target element cursor(\[11:Element ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MC _ManualCleanup _2QuadToQuad([11:1047, 11:1045])
```
