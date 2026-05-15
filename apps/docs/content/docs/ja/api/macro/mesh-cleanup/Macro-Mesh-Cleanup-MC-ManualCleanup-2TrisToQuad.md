---
title: "MC _ManualCleanup _2TrisToQuad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Merge two Tri element into one Quad element

## Syntax

```psj
MC _ManualCleanup _2TrisToQuad(Cursor[] elements)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Array of only 2 Tri elements

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MC _ManualCleanup _2TrisToQuad([11:1068,11:1066])
```
