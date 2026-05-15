---
title: "ChangeEntityColor()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Change the colors of the selected entities.

## Syntax

```psj
ChangeEntityColor(Cursor[], color entityColor)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

A list of entity to change color.

<!-- @since:5.1.0 -->
### 2. Color

Specify the color to change.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ChangeEntityColor([11:703,11:704], 8421440)
```
