---
title: "ChangeEntityEdgeColor()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Change the color of the edges of selected entity.

## Syntax

```psj
ChangeEntityEdgeColor(Cursor[] crParts, COLORREF col, bool bRandom)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

A list of part.

<!-- @since:5.1.0 -->
### 2. color

Specify a color to set.

<!-- @since:5.1.0 -->
### 2. bool

Flag of random color

- "1": Edge color is set at random.
- "0": Edge color is set by specified color.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ChangeEntityEdgeColor([3:1], 16711746, 0)
```
