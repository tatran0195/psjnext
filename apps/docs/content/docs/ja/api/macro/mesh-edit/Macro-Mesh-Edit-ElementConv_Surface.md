---
title: "ElementConv _Surface()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Element Conversion for surface elements in a aper..

## Syntax

```psj
ElementConv _Surface(cursor[] taBody, int iType)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor\[]

Target body cursor(\[3:Part ID])

<!-- @since:5.1.0 -->
### 2. Int

Conversion Type

- 0: To Linear(Tri3/Quad4)
- 1: To Quadratic(Tri6/Quad8)
- 2: Tri3
- 7: Split(Tri6to4Tri3s/Quad8to4Quad4s)

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ElementConv _Surface([3:2], 1)
```
