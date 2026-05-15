---
title: "MergePart()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Merge Part

## Syntax

```psj
MergePart(double tolerance, bool removeShareFace, cursor[] part)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

Insert tolerance value (m)

<!-- @since:5.0.1 -->
### 2. Bool

Whether remove share face or not True = 1, No =0

<!-- @since:5.0.1 -->
### 3. Cursor\[]

Target parts cursor(\[3:Part ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
MergePart(1e-08, 1, [3:4, 3:1])
```
