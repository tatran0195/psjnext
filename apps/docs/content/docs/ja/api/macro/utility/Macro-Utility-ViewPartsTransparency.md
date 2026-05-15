---
title: "ViewPartsTransparency()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Change the color of the selected part.

## Syntax

```psj
ChangeBodyColor(Cursor[] parts, double transparency)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

A list of cursor specify parts.

<!-- @since:5.1.0 -->
### 2. double

Specify transparency of the parts.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ViewPartsTransparency([3:1], 0.2)
```
