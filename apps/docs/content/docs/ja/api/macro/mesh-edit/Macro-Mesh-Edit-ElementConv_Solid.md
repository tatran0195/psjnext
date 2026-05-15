---
title: "ElementConv _Solid()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Element Conversion for solid elements in a part.

## Syntax

```psj
ElementConv _Solid(cursor[] taBody, int iType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

Target body cursor(\[3:Part ID])

<!-- @since:5.1.0 -->
### 2. Int

Conversion Type

- 0: To Linear(Tet4/Penta5/Hex8/Pyramid5)
- 1: To Quadratic(Tet10/Penta15/Hex20/Pyramid13)
- 2: Hexa to Penta5
- 3: Hexa/Penta to Tet4

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ElementConv _Solid([3:2], 1)
```
