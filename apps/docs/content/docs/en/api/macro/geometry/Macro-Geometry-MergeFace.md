---
title: "MergeFace()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Merge Face

## Syntax

```psj
MergeFace(Cursor[] face,bool merge _edge)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Face List

<!-- @since:5.0.1 -->
### 2. Bool

Auto Merge Edge 1=Yes,0=No

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MergeFace([6:24, 6:26], 0)
```
