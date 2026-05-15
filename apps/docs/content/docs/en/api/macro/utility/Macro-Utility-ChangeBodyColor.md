---
title: "ChangeBodyColor()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Change the color of the selected part.

## Syntax

```psj
ChangeBodyColor([Cursor, color][] bool bResetFaceColor)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. \[Cursor, color]\[]

A list of pair of part and its color.

<!-- @since:5.1.0 -->
### 2. bool

Specify whether or not reset face color.

- "1": Reset face color.
- "0": Keep face color.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ChangeBodyColor([[3:1, 16777193]], 0)
```
