---
title: "SquareUpFillet()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Scale Up Fillet

## Syntax

```psj
SquareUpFillet(cursor[] vcrFaces)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Fillet face list cursor (\[6: Face ID])

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SquareUpFillet([6:21, 6:26, 6:54])
```
